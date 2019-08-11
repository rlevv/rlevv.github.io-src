#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ryan Levitt'
SITENAME = 'Ryan Levitt\'s Coding Blog'
SITEDESCRIPTION = 'Projects.'
SITEURL = 'http://localhost:8000'

PATH = 'content'
PAGE_PATHS = ['pages']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


THEME = 'theme'
STATIC_PATHS = ['images', 'static', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/header.jpg': {'path': 'header.jpg'},
}
HEADER = 'images/header.jpg'

# Blogroll
#LINKS = (('Projects', 'https://rlevv.github.io/tag/projects.html'))

# Social widget
SOCIAL = (('github', 'https://github.com/rlevv'), 
          ('mail', 'mailto:rlevitt97@gmail.com'),
          ('linkedin', 'https://www.linkedin.com/in/rlevv/'),
          ('stackoverflow', 'https://stackoverflow.com/users/10782802/rlevv'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True