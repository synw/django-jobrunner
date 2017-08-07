import time
from terminal.commands import jprint


def run():
    i = 0
    while i < 100:
        msg = " Job 2: " + str(i)
        jprint(msg)
        time.sleep(0.4)
        i += 1