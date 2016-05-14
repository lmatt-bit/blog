#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'lmatt'
SITENAME = u'do not know'
SITEURL = 'http://lmatt-bit.github.io/blog'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         #('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (#('social link', '#'),
          #('Another social link', '#'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = '../pelican-themes/Flex'

PLUGIN_PATHS=['../pelican-plugins', './plugins']
#PLUGINS=['disqus_static', 'pelican_gist', 'liquid_tags.notebook']
PLUGINS=['ipynb.markup']
MARKUP = ('md', 'ipynb')

#NOTEBOOK_DIR='notebooks'

DISQUS_SITENAME='lmattbit'
DISQUS_SECRET_KEY='rB2wbazGTv3QE7X7LjSQQOLIuvOSKzPfMCBw8LR7OQvckPQWrAPA6I0DKIPfRV51'
DISQUS_PUBLIC_KEY='XDvnhdAsVekBPEIrHocRDlOad2H6KT6M301MB082EZT9zoUKIg9QDphQb4hFSMtE'
