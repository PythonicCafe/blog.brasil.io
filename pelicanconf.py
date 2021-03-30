#!/usr/bin/env python

import glob
import json
import os

AUTHOR = "Álvaro Justen"
SITENAME = "Brasil.IO - Blog"
SITESUBTITLE = "Dados abertos para mais democracia"
SITEURL = "https://blog.brasil.io"
SITEIMAGE = "/theme/images/logo-blog.brasil.io.png"
STATIC_PATHS = ["extra", "images"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

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

# Method to call elements from json files
def get_authors_data(path):
    dict = {}
    for f in glob.glob(path):
        dict[os.path.basename(f).split('.')[0]] = json.load(open(f, 'r', encoding='utf-8'))
    return dict

AUTHOR_DETAIL = get_authors_data('content/authors/*.json')

# Blogroll
LINKS = (
    ("Blog", "https://blog.brasil.io/"),
    ("Datasets", "https://brasil.io/datasets"),
    ("Colabore", "https://brasil.io/colabore"),
    ("Contato", "https://brasil.io/contato"),
)

DEFAULT_PAGINATION = 10
TYPOGRIFY = True
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


MARKUP = ("md", "ipynb")
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {
            "anchorlink": True,
            "baselevel": 2,
            "permalink": False,
        },
    },
    "output_format": "html5",
}

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]
IPYNB_MARKUP_USE_FIRST_CELL = True
IGNORE_FILES = [".ipynb_checkpoints"]

THEME = "themes/pelican-alchemy/alchemy"

DISQUS_SITENAME = "brasilio"
GOOGLE_ANALYTICS = "UA-117698282-2"
