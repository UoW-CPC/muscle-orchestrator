import sys

sys.path.append("../")
from app.lib.logsys import Log
from app.lib.filesystem import Filesystem
from app.lib.system import System

def main():
    Log.info('---------------------')
    Log.info('Profiler task Starts')
    Log.info('---------------------')
    files = Filesystem.getFiles()
    Log.info("List of afas files:")
    for file in files:
        Log.info(file)
    Log.info('Merging the files with MUSCLE profile option')
    filesNumber = len(files)
    count = 0
    while count < filesNumber:
        if count == 0:
            Log.info('Profiling the first two files..')
            print(files[count], files[count + 1], '../data/profile/temp-' + str(count+1) + '.afas')
            (ret, out, err) = muscle(files[count], files[count + 1], '../data/profile/temp-' + str(count+1) + '.afas')
            Log.info("return, {}".format(ret))
            Log.info("output, {}".format(out))
            Log.error("error, {}".format(err))
        elif filesNumber == count + 1:
            Log.info('Profiling the last file..')
            print(files[count], '../data/profile/temp-' + str(count - 1) + '.afas','../data/final/result.afas')
            (ret, out, err) = muscle(files[count], '../data/profile/temp-' + str(count - 1) + '.afas','../data/final/result.afas')
            Log.info("return, {}".format(ret))
            Log.info("output, {}".format(out))
            Log.error("error, {}".format(err))
        elif filesNumber >= count + 3:
            Log.info('Profiling a single file..')
            print(files[count+1], '../data/profile/temp-' + str(count) + '.afas', '../data/profile/temp-' + str(count+1) + '.afas')
            (ret, out, err) = muscle(files[count+1], '../data/profile/temp-' + str(count) + '.afas', '../data/profile/temp-' + str(count+1) + '.afas')
            Log.info("return, {}".format(ret))
            Log.info("output, {}".format(out))
            Log.error("error, {}".format(err))
        count = count + 1
    Log.info('Please see the results in folder data/final')
    Log.info('------------------------')
    Log.info('Profiler task Completes')
    Log.info('------------------------')


def muscle(in1, in2, out):
    (ret, out, err) = System.command(
        ['bin/muscle', '-profile',
         '-in1', in1,
         '-in2', in2,
         '-out', out])
    return ret,out,err

if __name__ == "__main__":
    main()
