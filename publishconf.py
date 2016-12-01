#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.vandorp.biz'

FEED_ALL_ATOM = 'feeds/all.atom.xml'

SOCIAL = SOCIAL + (('rss', SITEURL + '/' + FEED_ALL_ATOM),)

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = 'vandorpit'
GOOGLE_ANALYTICS = 'UA-24228873-1'
ADDTHIS_PROFILE = 'ra-4d779d493e48b954'

RELATIVE_URLS = False
