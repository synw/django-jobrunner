from __future__ import print_function
import subprocess
from django.core.management.base import BaseCommand
from django.conf import settings
from instant.conf import CENTRIFUGO_HOST, CENTRIFUGO_PORT, SECRET_KEY
from jobrunner.conf import INPUT_CHAN, OUTPUT_CHAN, VERBOSITY

addr = CENTRIFUGO_HOST.replace("http://", "") + ":" + str(CENTRIFUGO_PORT)


class Command(BaseCommand):
    help = "Launch the jobs runner"

    def handle(self, *args, **options):
        global addr
        c = settings.BASE_DIR + '/jobrunner/run'
        cmd = [c, "-path", settings.BASE_DIR, "-addr",
               addr, "-key", SECRET_KEY, "-cmd_in", INPUT_CHAN, "-cmd_out", OUTPUT_CHAN, "-v", str(VERBOSITY)]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in p.stdout:
            msg = str(line).replace("b'", "")
            msg = msg[0:-3]
            print(msg)
        p.wait()
