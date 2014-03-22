#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://vandorp.biz'

FEED_ALL_ATOM = 'feeds/all.atom.xml'

SOCIAL = SOCIAL + (('rss', SITEURL + '/' + FEED_ALL_ATOM),)

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = 'dandydev'
# GOOGLE_ANALYTICS = 'UA-24099413-2'
# ADDTHIS_PROFILE = 'ra-4f274b9c7023574d'

RELATIVE_URLS = False