import logging
import re

from pelican import contents, signals

log = logging.getLogger(__name__)

ERT_WPM = 300  # words per minute by default
ERT_FORMAT = '{min_time}-{max_time}'


def initialize(gen):
    global ERT_WPM, ERT_FORMAT
    for option in ['ERT_WPM', 'ERT_FORMAT']:
        if not option in gen.settings.keys():
            log.warning(
                'The necessary config option is missing: {},\
 using default value: \'{}\''.format(option, globals()[option])
            )
        else:
            globals()[option] = gen.settings[option]


def strip_tags(content):
    return re.sub(u'<!--.*?-->|<[^>]*>', '', content)


def estimate(text):
    minutes = round(len(strip_tags(text).split()) / ERT_WPM)
    return ERT_FORMAT.format(min_time=minutes, max_time=round(minutes*1.5))


def ert(obj):
    if obj._content:
        obj.ert = estimate(obj._content)


def register():
    signals.article_generator_init.connect(initialize)
    signals.content_object_init.connect(ert)
