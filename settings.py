#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Mawuli Adzaku'
SITENAME = u'Takataka'
SITEURL = 'http://takataka.com'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Igor Sobreira', 'http://igorsobreira.com/'),
          ('Electric Duncan', 'http://technicae.cogitat.io/'),
          ('Ned Batchelder', 'http://nedbatchelder.com/text/whirlext.html'),
	  ('http://igorsobreira.com/','http://research.microsoft.com/en-us/um/people/simonpj/Papers/marktoberdorf/'),
	  ("An explorer's log",'http://nakkaya.com/'),
	  ('Machine Learning for Beginners « Ian Ma','http://ianma.wordpress.com/2009/07/19/machine-learning-for-beginners/'),
          ('Add more links', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/mawuli_ypa'),
         ('github','http://github.com/mawuli_ypa'),
        ('google', 'https://plus.google.com/101891019344348512650/about'),
        )

DEFAULT_PAGINATION = 10

TWITTER_USERNAME = "@mawuli_ypa"
GITHUB_URL = "http://github.com/mawuli-ypa"
DISQUS_SITENAME = "mawuli"


# Menuitems
MENUITEMS =  (('Weblog', '/'),)


ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
