import time
from terminal.commands import jprint


def run():
    i = 0
    while i < 50:
        msg = " Job 0: " + str(i)
        jprint(msg)
        time.sleep(0.5)
        i += 1
