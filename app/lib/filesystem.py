import re
from os import listdir

from app.lib.logsys import Log

class Filesystem:

    @classmethod
    def getFiles(cls):
        filesTemp = []
        files = []
        try:
            filesTemp = listdir('../data/output')
        except  EnvironmentError as e:
            Log.error('Input file error:')
            Log.error(e)
            Log.exit()
        for file in filesTemp:
            if re.search('.*afas$',file):
                files.append('../data/output/'+file)
        files.sort()
        return files