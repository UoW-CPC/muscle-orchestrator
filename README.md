# muscle-orchestrator

## Introduction
This application is a parallel implementation of the MSA (Multiple Sequence Alignment) tool [MUSCLE](https://www.drive5.com/muscle/).

MUSCLE is an well-known tool that utilises a single core to perform MSA analysis. To improve performance, MUSCLE is being parallelised by utilising [Docker](https://www.docker.com/).
With this approach MUSCLE runs on several [containers](https://www.docker.com/resources/what-container) and each container analyse a different set of data.

To more detail, the application implements the parallel solution in three phases:
1. Split the dataset (fas file) into smaller datasets (fas files) of 50 sequences.
2. Parallel execution of MUSCLE into several containers. Each container analyses a different dataset.
3. Merge the output of these MUSCLE container (afas files) with the MUSCLE profile option, and get the final output (afas file).

__Expected performance:__
In case that the working machine analyse X sequences in T minutes, with the above process the performance gain for N parallel containers is approximately ( N * X ) sequence in T minutes.

## Getting Started Guide

This guide introduces two use cases:
1. A __Cloud Solution__ with [MiCADO Scale](https://micado-scale.eu/). MiCADO Scale is develop under the EU project [COLA](https://project-cola.eu/). Requires MiCADO Scale, for installation instructions see [here](https://micado-scale.readthedocs.io/en/latest/).
2. A __Standalone Solution__ for a single working machine. Requires Docker, for instalation instructions see [here](https://docs.docker.com/get-docker/).

__Important:__ This guide includes sections with instructions for each use case. Please review sections _Cloud Solution_ and _Standalone Solution_ before you continue.


### Downloading the application
The first step is to download the application in your working environment.
To do so, use the download link, or run the following command in your terminal:
 ```
git clone https://github.com/UoW-CPC/muscle-orchestrator.git
 ```

Then move into muscle-orchestrator folder.
 ```
cd muscle-orchestrator
 ```

There by using the command:
 ```
ls
 ```
You can see three folders and one file:
* __app__ - folder - contains Python scripts, MUSCLE binaries and a Java tool (only for Cloud Solution) to perform the various phases.
* __data__ - folder - contains data used by MUSCLE.
* __logs__ - folder - contains application logs.
* __README.md__ - folder - application guide.


### Phase 1 - Split the dataset

 __Important:__ Python 3 is required.

 ```
 python3 -f /PATH_TO_THE_DATASET
 # Sample command: python3 -f /data/full_dataset.fas
 ```
 This sample command performs several steps:
 1. Reads the file full_dataset.fas from the folder 'data'.
 2. Splits the dataset in fas files of 50 sequences and save the files in folder 'data/input'.
 3. Adds a prefix to the input files, e.g. in-1-full_dataset.fas, in2-2-full_dataset.fas
 4. Creates a log file into the folder 'logs'. Log filename: muscle-orchestrator.log.

 Example: In case the full_dataset.fas file contains 120 sequences, this result to three files in the input folder:
 * in-1-full_dataset.fas, file that contains 50 sequences, 1 to 50
 * in-2-full_dataset.fas, file that contains 50 sequences, 51 to 100
 * in-3-full_dataset.fas, file that contains 20 sequences, 101 to 120


 ### Phase 2 - MUSCLE parallel execution

In this phase we perform MSA for the files created in the previous step. From the proposed solutions choose the one that fits to your needs.

#### Cloud Solution

To follow this solution, jQueuer application needs to be deployed through MiCADO in a Cloud environment.
A MiCADO Scale deployment guide is not in the scope of this guide. Please, feel free to ask for guidance by contacting us [here](https://micado-scale.eu/contact/).

__Notice__: jQueuer is an application that creates a queue of jobs and sends these jobs to MiCADO worker nodes. The worker nodes execute the jobs and when a job completes jQeuer send another job from the queue.
This allow us to automate the process by defining several jobs and start them in multiple worker nodes.

If you have jQeuer deployed through MiCADO, follow this steps to perform your MSA:

1. Create a jQueuer expirement file.
__Important:__ Java 8 is required

 ```
 java
 ```
2. Take the output.json file from the folder... and sumbit it to the jQueuer web interface.
This process instruct the worker node to run MUSCLE into a container and defines the input data.
3. For every MUSCLE container we see an output file out-1-
4. For every MUSCLE container we see a log file in
5. When all jobs are completed you will have an output file for each input file.

Your can now go to phase 3 and merge the results with MUSCLE profile option.

#### Standalone Solution
Here we don't have jQueuer and MiCADO to automate the process for us; therefore we manually start MUSCLE containers for all the input files.

__Warning:__ each container requires resources, so run in paraller as many containers you system can handle.
Manual start a MUSCLE container for each file.
1. Define input
2. Run a container
3. for MUSCLE container we see an output file out-1-
4. for MUSCLE container we see a log file in
5. Repeat steps 1-4 until you finish your analysis. When all jobs are completed you will have an output file for each input file.



### Phase 3 - Merge the outputs with MUSCLE profile.

Final step of the process:

python3 profile_output.py
 __Important:__ Your dataset must contain more than 100 sequences. Otherwise you might get unexpected results