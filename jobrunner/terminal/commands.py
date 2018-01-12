from __future__ import print_function
from term.commands import Command, rprint
from jobrunner.producers import runjob


def job(request, cmd_args):
    if request.user.is_superuser:
        print("JOB", cmd_args)

        jobname = cmd_args[0]
        jobid = cmd_args[1]
        errmsg = runjob(jobname, jobid)
        if errmsg is not None:
            rprint("ERROR sending the job to the runner:", errmsg)


c0 = Command("job", job, "Start an asynchronous job")

COMMANDS = [c0]
