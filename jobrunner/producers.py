from instant.producers import publish
from jobrunner.conf import INPUT_CHAN


def runjob(jobname, jobid):
    err = publish(message="job", data={"uid": jobid,
                                       "cmd": jobname}, channel=INPUT_CHAN)
    return err
