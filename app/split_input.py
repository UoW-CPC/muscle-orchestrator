import sys
import math

sys.path.append("../")
from app.lib.input import Input
from app.lib.logsys import Log

def main():
    Log.info('------------------')
    Log.info('Split Task Starts')
    Log.info('------------------')
    inputArgs = sys.argv
    args = inputArgs[1:]
    filePath, fileName = Input.getValues(args)
    Log.info('Path:')
    Log.info(filePath)
    Log.info('File name:')
    Log.info(fileName)
    try:
        with open(filePath) as f:
            lines = sum(1 for _ in f)
    except  EnvironmentError as e:
        Log.error('Input file error:')
        Log.error(e)
        Log.exit()
    Log.info('Number of sequences:')
    Log.info(lines/2)
    Log.info('The dataset is being split in files of 50 sequences.')
    Log.info('Total files:')
    filesNumber = math.ceil(lines/100)
    Log.info(filesNumber)
    filesList = []
    count = 0
    Log.info('File names:')
    while count < filesNumber:
        count += 1
        filesList.append('in-'+str(count)+'-'+fileName)
    for file in filesList:
        Log.info(file)
    try:
        lineCount = 0
        filesCount = 0
        input = open(filePath,"r")
        for line in input:
            if lineCount % 100 == 0:
                try:
                    output.close()
                except:
                    Log.info('Start splitting the dataset..')
                output = open('../data/input/' + filesList[filesCount], "a")
                filesCount = filesCount + 1
            output.write(line)
            lineCount = lineCount + 1
        input.close()
        Log.info('Finish splitting the dataset..')
    except  EnvironmentError as e:
        Log.error('Unkown error:')
        Log.error(e)
        Log.exit()
    Log.info('---------------------')
    Log.info('Split Task Completes')
    Log.info('---------------------')

if __name__ == "__main__":
    main()
