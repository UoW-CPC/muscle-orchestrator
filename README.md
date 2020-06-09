# muscle-orchestrator

## Introduction
This application is a parallel implementation of the MSA (Multiple Sequence Alignment) tool [MUSCLE](https://www.drive5.com/muscle/).

MUSCLE is an well-known tool that utilises a single CPU core to perform MSA. To improve performance, MUSCLE is being parallelised by utilising [Docker](https://www.docker.com/).
With this approach MUSCLE runs on several [containers](https://www.docker.com/resources/what-container) and each container analyse a different set of data.

To more detail, the application implements the parallel solution in three phases:
1. Split the dataset (fas file) into smaller datasets (fas files) of 50 sequences.
2. Parallel execution of MUSCLE into several containers. Each container analyses a different dataset.
3. Merge the output of these MUSCLE container (afas files) with the MUSCLE profile option, and get the final output (afas file).

__Expected performance:__
In case that the working machine analyse X sequences in T minutes, with the above process the performance gain for N parallel containers is approximately ( N * X ) sequence in T minutes.

## Getting Started Guide

This guide introduces two use cases:
1. A __Cloud Solution__ with [MiCADO Scale](https://micado-scale.eu/). MiCADO Scale is develop under the EU project [COLA](https://project-cola.eu/). For installation instructions see [here](https://micado-scale.readthedocs.io/en/latest/).
2. A __Standalone Solution__ for a single working machine with Docker. For installation instructions see [here](https://docs.docker.com/get-docker/).

__Important:__ This guide includes sections with different instructions for each use case. Please review sections _Cloud Solution_ and _Standalone Solution_ to help you choose which use case fulfils your requirements.


### Downloading the application
The first step is to download the application in your working environment.
To do so, use the download link, or run the following command in your terminal:
 ```
git clone https://github.com/UoW-CPC/muscle-orchestrator.git
 ```

Then move into muscle-orchestrator folder:
 ```
cd muscle-orchestrator
 ```

There by using the command:
 ```
ls
 ```
You can see three folders and one file:
* __app__ - folder - contains Python scripts, MUSCLE binaries and a Java tool (for the Cloud use case).
* __data__ - folder - contains data used by MUSCLE, and containers logs.
* __logs__ - folder - contains application logs.
* __README.md__ - file - application guide.


### Phase 1 - Split the dataset

 __Important:__ Python 3 is required

 ```
 # move to the app directory
 cd app
 python3 split_input.py -f /PATH_TO_THE_DATASET
 # Sample command: python3 split_input.py -f ../data/dataset.fas
 # move again to the parent directory
 cd ..
 ```
 This sample command performs several actions:
 1. Reads the file 'dataset.fas' from the folder 'data'.
 2. Splits the dataset in fas files of 50 sequences and save the files in folder 'data/input'.
 3. Adds a prefix to the input files, e.g. 'in-1-dataset.fas', 'in-2-dataset.fas'.
 4. Writes details related to this process to a log file into the folder 'logs'. Log filename: muscle-orchestrator.log.

 __Example:__ In case the 'dataset.fas' file contains 120 sequences, this result to three files in the input folder:
 * in-1-dataset.fas, file that contains sequences 1 to 50.
 * in-2-dataset.fas, file that contains sequences 51 to 100.
 * in-3-dataset.fas, file that contains sequences 101 to 120.


 ### Phase 2 - MUSCLE parallel execution

In this phase we perform MSA for the files created in the previous step. As mention previously from the two use case choose the one that fulfills your requirements.

#### Cloud Solution

To follow this solution, jQueuer application needs to be deployed through MiCADO in a Cloud environment.
A MiCADO Scale deployment guide is not in the scope of this guide. Please, feel free to ask for guidance by contacting us [here](https://micado-scale.eu/contact/).

__Notice__: jQueuer is an application that creates a queue of jobs and sends these jobs to MiCADO worker nodes. The worker nodes execute the jobs and when a job completes jQeuer send another job from the queue.
This allow us to automate the process by defining several jobs and start them in multiple worker nodes.

If you have jQeuer deployed through MiCADO, follow these steps to perform your MSA:

Create a jQueuer expirement file:

__Important:__ Java 8 and above is required

 ```
 # Move to the data/bin folder
 cd data/bin
 # Create the JSON file
java -jar files-to-jobs.jar ../../data/input/ jobs.json
 # Move back to the project parent folder
 cd ../..
 ```
Take the jobs.json file from the 'app/bin' folder and submit it to the jQueuer web interface.
jQueuer starts instructing the worker nodes to run MUSCLE into containers and passes to them parameters for input and output data.

For every MUSCLE container we see an output file in the folder 'data/output', e.g. out-1-dataset.afas.

For every MUSCLE container we see a log file in the folder 'data/logs'. In this folder there is one log file for each container you start. These log files contain information about input/output files, and the MUSCLE processes.

When all jobs are completed you will have an output file for each input file.

You can now go to phase 3 and merge the results with the MUSCLE profile option.

#### Standalone Solution

In this scenario you manually start a MUSCLE container for every input file.

Starting a MUSCLE container:

 ```
 # Move to the data folder
 cd data
 # Run a MUSCLE container for a single file
 sudo docker run -it -v ${PWD}:/muscle/data/ dkagialis/muscle /muscle/app/execute.sh ../data/input/FILENAME
 # Sample command: sudo docker run -it -v ${PWD}:/muscle/data/ dkagialis/muscle /muscle/app/execute.sh ../data/input/in-1-dataset.fas
 # Move back to the parent folder
 cd ..
 ```

 The container initiates a MUSCLE process, takes as an input the given file, and writes the output in the folder 'data/output'. The process changes the prefix from 'in' to 'out' in the output file, e.g. out-1-dataset.afas in our example.

 Repeat the above steps until you analyse all your files. When all jobs are completed you will have an output file for each input file.

__Warning:__ Each container requires resources to run, so run in parallel as many containers your system can handle.

You can view the logs for this process in the folder 'data/logs'. In this folder there is one log file for each container you start. These log files contain information about input/output files, and the MUSCLE processes.

You can now go to phase 3 and merge the results with the MUSCLE profile option.

### Phase 3 - Merge the outputs with MUSCLE profile.

Having completed phase 2, in the folder 'data/output' there are several afas file (one for each input file). At this point the MUSCLE profile option is being used to merge all these files.

The above process is being performed by this application. The application iteratively parses all the files in the output folder and initiates MUSCLE as many times is required to merge all the afas into a single afas file.

MUSCLE profile:

 ```
 # Move to the app folder
 cd app
python3 profile_output.py
 ```
__Notice:__ The application is designed to work in a linux platform. In case you want to change platform to Mac OSX or MS Windows put the MUSCLE tool into the folder 'app/bin' and rename it to 'MUSCLE'.

 The above script performs several actions:
 1. Passes to the MUSCLE the first two files from the 'data/output' folder and writes the output 'temp-1.afas' in the 'data/profile' folder.
 2. Passes to the MUSCLE the third file from the 'data/output' folder and the 'temp-1.afas' from the 'data/profile', and writes the output 'temp-2.afas' in the 'data/profile' folder.
 3. Repeat the 2 step until all files have been processed.
 4. In the last iteration in step 3 MUSCLE takes as input the last file from the 'data/output' folder and the last file created in the 'data/profile', and writes the output 'results.afas' to the folder 'data/result'.
 5. Writes details related to this process to a log file into the folder 'logs'. Log filename: muscle-orchestrator.log.

 __Important:__ Your dataset must contain more than 100 sequences. Otherwise you might get unexpected results.


