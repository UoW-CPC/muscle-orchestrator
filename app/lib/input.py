import getopt
import os

from app.lib.logsys import Log

class Input:

    @classmethod
    def getValues(cls, inputArgs):
        Log.info("input arguments: {}".format(inputArgs))
        options = "f:"
        longOptions = ["file="]
        try:
            opts, args = getopt.getopt(inputArgs, options, longOptions)
        except getopt.GetoptError as err:
            Log.error(err)
            Log.exit()

        fileFlag = False
        filePath = None
        fileName = None

        for opt, arg in opts:
            Log.info("processing option: {} with arguments: {}".format(opt,arg))
            if opt in ("-f", "--file"):
                if fileFlag:
                    Log.error("Input Error. Can't pass one argument twice. Exiting the application..")
                    Log.exit()
                else:
                    fileFlag = True
                    filePath = arg
                    fileName = cls.fileInput(arg)

        if fileFlag is False:
            Log.error("Input Error. You must specify a valid file. Exiting the application..")
            Log.exit()

        return filePath,fileName

    @classmethod
    def fileInput(cls, arg):
        fileName = os.path.basename(arg)
        return fileName
