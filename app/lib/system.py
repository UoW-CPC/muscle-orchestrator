from app.lib.logsys import Log
import subprocess

class System:
    @classmethod
    def command(cls, args_list):
        Log.info('Running system command: {0}'.format(' '.join(args_list)))
        proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s_output, s_err = proc.communicate()
        s_return = proc.returncode
        return s_return, s_output, s_err