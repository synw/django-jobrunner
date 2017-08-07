from __future__ import print_function
from terminal.commands import Command, jprint
from jobrunner.producers import runjob


def job(request, cmd_args):
    print("ARGS", cmd_args)
    if request.user.is_superuser:
        jobname = cmd_args[0]
        jobid = cmd_args[1]
        err = runjob(jobname, jobid)
        if err is not None:
            jprint("ERROR sending the job to the runner:", err)


c0 = Command("job", job, "Start an asynchronous job")

COMMANDS = [c0]
