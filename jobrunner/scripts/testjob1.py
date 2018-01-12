import time
from term.commands import rprint


def run():
    i = 0
    while i < 70:
        msg = " Job 1: " + str(i)
        rprint(msg)
        time.sleep(0.6)
        i += 1