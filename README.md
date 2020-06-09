# muscle-orchestrator

## Introduction
This application is a parallel implementation of the MSA (Multiple Sequence Alignment) tool [MUSCLE](https://www.drive5.com/muscle/).

MUSCLE is an established tool that utilises a single core to perform the analysis. To improve performance, MUSCLE is being parallelised by utilising [Docker](https://www.docker.com/).
With this approach MUSCLE runs on several [containers](https://www.docker.com/resources/what-container) and each container analysis a different set of data.

To more detail, the application implements the parallel solution in three phases:
1. Split the dataset (fas file) into smaller datasets (fas files) of 50 sequences.
2. Parallel execution of MUSCLE into several containers. Each container will analyse a different dataset.
3. Merge the output of these MUSCLE processes (afas files) with the MUSCLE profile option, and get the final output (afas file).

__Expected performance:__
In case that the working machine analysis X sequences in T minutes, with the above process the performance gain for N parallel containers is approximately ( N * X ) sequence in T minutes.

## Getting Started Guide

This guide introduces two use cases:
1. A deadline-based __Cloud Solution__ with [MiCADO Scale](https://micado-scale.eu/). MiCADO Scale is develop under the EU project [COLA](https://project-cola.eu/) Cloud Orchestration at the Level of the Application. Requires MiCADO Scale, [Installation guide](https://micado-scale.readthedocs.io/en/latest/).
2. A __Standalone Solution__ for a single working machine. Requires Docker, [Installation guide](https://docs.docker.com/get-docker/).

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
* __app__ - folder - contains the tools
* __data__ - folder -
* __logs__ - folder -
* __README.md__ - folder -

### Cloud Solution

### Standalone Solution