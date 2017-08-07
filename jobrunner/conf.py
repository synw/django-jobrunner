from django.conf import settings


SITE_SLUG = getattr(settings, "SITE_SLUG")
INPUT_CHAN = getattr(settings, 'JOBS_INPUT_CHAN', '$' + SITE_SLUG + "_jobs")
OUTPUT_CHAN = getattr(settings, 'JOBS_OUTPUT_CHAN',
                      '$' + SITE_SLUG + "_command")
VERBOSITY = getattr(settings, "JOBS_VERBOSITY", 1)
