#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Daniel van Dorp'
SITENAME = u'Van Dorp IT'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GITHUB_USER = 'djvdorp'
GITHUB_SKIP_FORK = True

STATIC_PATHS = ['images', 'files', 'extra/robots.txt', 'extra/favicon.ico']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Blogroll
LINKS = (('SamMobile', 'https://www.sammobile.com/team/'),
         ('VirtKick', 'https://www.virtkick.com/people.html'),
         ('LowEndTalk', 'http://lowendtalk.com/profile/571/djvdorp'),
         ('Linux Audit', 'https://linux-audit.com'),
         ('Debian Handbook', 'https://debian-handbook.info'),
         ('cron.weekly', 'https://www.cronweekly.com'),
         ('Samantha de Blij', 'http://www.samanthadeblij.nl'),
         ('DandyDev', 'http://www.dandydev.net'),
         ('All Things Pretty', 'http://www.allthingspretty.nl'),
         ('Nadine Herbert', 'http://www.nadineherbert.nl'),
)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/djvdorp'),
          ('linkedin', 'https://www.linkedin.com/in/danielvandorp'),
          ('github', 'http://github.com/djvdorp'),
          ('facebook', 'http://facebook.com/djvdorp'),
)

DEFAULT_PAGINATION = 5

TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_TAGS_ON_SIDEBAR = True

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid']

THEME = os.path.join(os.environ.get('HOME'), 'dev/pelican-bootstrap3')

BOOTSTRAP_THEME = 'superhero'

USE_OPEN_GRAPH = True
OPEN_GRAPH_FB_APP_ID = '1399075273698546'
OPEN_GRAPH_IMAGE = 'images/vandorpit.jpg'

CC_LICENSE = "CC-BY-NC-SA"

PYGMENTS_STYLE = 'monokai'

PLUGIN_PATHS = [os.path.join(os.environ.get('HOME'), 'dev/pelican-plugins')]

DISQUS_SITENAME = 'vandorpit-dev'
ADDTHIS_PROFILE = 'ra-532db7234d3d5a6e'

DISQUS_DISPLAY_COUNTS = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
