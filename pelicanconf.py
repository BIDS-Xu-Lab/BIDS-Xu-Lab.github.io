"""Pelican Configuration

For Hua Xu Lab
"""
import json
from datetime import datetime
import re
from jinja2 import Template

AUTHOR = 'Huan He'
SITENAME = 'Clinical NLP Lab'
SITEDESCRIPTION = "Clinical NLP Lab"

# just set this to relative path due to deployment issue
SITEURL = '.'
SITE_EMAIL = 'TBD'

# where to store the markdown contents and other materials
PATH = 'content'

# I'm here
TIMEZONE = 'America/New_York'

# by default
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# customized plugins
PLUGINS = [
    'myplugins'
]

# Social widget if needed.
# SOCIAL = (('https://twitter.com/', '#'),
#           ('https://facebook.com/', '#'),)

# we don't need pagination as there is no blog
DEFAULT_PAGINATION = False

# put all contents under year folder
ARTICLE_URL = "{date:%Y}-{slug}.html"
ARTICLE_SAVE_AS = "{date:%Y}-{slug}.html"

# for page
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

# for conference site author category is not needed
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

# no need for tags page
TAGS_URL = ""
TAGS_SAVE_AS = ""

# no need for archive page
ARCHIVES_SAVE_AS = ""

# no need for categorys page
CATEGORY_SAVE_AS = "{slug}.html"
CATEGORIES_SAVE_AS = "cates.html"

# current year of this site
CURRENT_YEAR = datetime.today().strftime('%Y')

# specify the customized theme
THEME = "./themes/lab-theme"

# load cache
LOAD_CONTENT_CACHE = True

# my works and each content
# links
LINKS = [
    ['GitHub', 'https://github.com/']
]

# get the template for a person
TEMPLATE_PERSON = Template(open('%s/templates/_person.html' % THEME).read())

# YEARS
REGEX_YEAR = r"\b(\d{4})\b"
def get_year(date_str):
    '''
    Get the year in a string
    '''
    ms = re.findall(REGEX_YEAR, date_str)

    if len(ms) == 0:
        return ''
    else:
        return ms[0]

# Get people
PEOPLE = json.load(open('content/team.json'))['people']
PEOPLE = list(filter(lambda p: p['uid']!= '', PEOPLE))
# PD = {}
# for p in PEOPLE:
#     if p['uid'] != '':
#         PD[p['uid']] = p