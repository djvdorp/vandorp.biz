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
LINKS = None

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/djvdorp'),)

DEFAULT_PAGINATION = 5

TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_TAGS_ON_SIDEBAR = True

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'nl2br', 'headerid']

THEME = os.path.join(os.environ.get('HOME'), 'Projects/pelican-bootstrap3')

BOOTSTRAP_THEME = 'superhero'

USE_OPEN_GRAPH = False
OPEN_GRAPH_FB_APP_ID = '20201859318270x'
OPEN_GRAPH_IMAGE = 'images/dandydev.png'

CC_LICENSE = "CC-BY-NC-SA"

PLUGIN_PATH = os.path.join(os.environ.get('HOME'), 'Projects/pelican-plugins')

DISQUS_SITENAME = 'dandydev-dev'
ADDTHIS_PROFILE = 'ra-520d4af6518bf3c7'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
