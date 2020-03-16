#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alephsa Team'
SITENAME = 'Alephsa'
SITESUBTITLE = 'Sustainable Imagination - Blog'
SITEURL = ''

PATH = 'content'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = 'en'
THEME = 'pelican-twitchy'

BOOTSTRAP_THEME = "united"
EXPAND_LATEST_ON_INDEX = True
SHARE = True
SOCIAL = (('Twitter', 'https://twitter.com/alephsa'), ('Bitbucket', 'https://bitbucket.org/alephsa'))
SITELOGO = 'images/logo.png'
HIDE_SITENAME = True
DISPLAY_PAGES_ON_MENU = True
CC_LICENSE = 'CC-BY-NC-SA'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['i18n_subsites', 'pelican-ipynb.markup']

IPYNB_USE_METACELL = True
IPYNB_SKIP_CSS = True

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]  

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'es': {
        'SITENAME': 'Alephsa',
        'THEME': 'pelican-twitchy_es',
        'SITESUBTITLE' : 'Imaginación Sostenible - Blog'
    }
}