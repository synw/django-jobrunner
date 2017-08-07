import time
from terminal.commands import jprint


def run():
    i = 0
    while i < 70:
        msg = " Job 1: " + str(i)
        jprint(msg)
        time.sleep(0.6)
        i += 1