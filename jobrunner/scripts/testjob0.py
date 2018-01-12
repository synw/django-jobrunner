import time
from term.commands import rprint


def run():
    i = 0
    while i < 50:
        msg = " Job 0: " + str(i)
        rprint(msg)
        time.sleep(0.5)
        i += 1
