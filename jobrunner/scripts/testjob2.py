import time
from term.commands import rprint


def run():
    i = 0
    while i < 100:
        msg = " Job 2: " + str(i)
        rprint(msg)
        time.sleep(0.4)
        i += 1