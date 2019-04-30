#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Álvaro Justen"
SITENAME = "Brasil.IO - Blog"
SITESUBTITLE = "Dados abertos para mais democracia"
SITEURL = "https://blog.brasil.io"
SITEIMAGE = "/theme/images/logo-blog.brasil.io.png"
STATIC_PATHS = ['extra/CNAME', 'images']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

PATH = "content"

TIMEZONE = "America/Sao_Paulo"
DEFAULT_LANG = "pt"
LOCALE = "pt_BR.UTF-8"

# Feed generation is usually not desired when developing
FEED_ALL_RSS = "feed.rss"
FEED_ALL_ATOM = "feed.atom"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Blog", "https://blog.brasil.io/"),
    ("Datasets", "https://brasil.io/datasets"),
    ("Colabore", "https://brasil.io/colabore"),
    ("Contato", "https://brasil.io/contato"),
)

# Social widget
SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = 10
TYPOGRIFY = True
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


MARKUP = ("md", "ipynb")

PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["ipynb.markup"]

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.
IGNORE_FILES = [".ipynb_checkpoints"]
THEME = "themes/pelican-alchemy/alchemy"

DISQUS_SITENAME = "brasilio"
GOOGLE_ANALYTICS = "UA-117698282-2"
