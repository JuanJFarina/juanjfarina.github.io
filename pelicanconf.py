AUTHOR = 'Juan José Farina'
SITENAME = 'Juan José Farina'
SITEURL = ""
SITESUBTITLE = "Software Engineer"

PATH = "content"

PLUGIN_PATHS = ["plugins"]
PLUGINS=['pelican-ert', 'share_post']

ERT_WPM = 170  # words per minute by default
ERT_FORMAT = '{min_time}-{max_time}'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/juanjosefarina"),
    ("GitHub", "https://github.com/JuanJFarina"),
    ("Youtube", "https://www.youtube.com/@juanjosefarina"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "notmyidea"

PAGE_ORDER_BY = 'date'
