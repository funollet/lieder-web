# -*- coding: utf-8 -*-
# Django settings for lieder project.

LIEDER_ROOT = '/home/jordif/code/lieder/'
SITE_URL = 'http://localhost:8000'  # required by verdjnlib.context_processors
ADMIN_MEDIA_CUSTOM_DIR = LIEDER_ROOT + 'media-admin/'
LOCAL_DEV = True

DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
    ('Jordi Funollet', 'jordi.f@ati.es'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3' # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = LIEDER_ROOT + 'lieder.sqlt'
 # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'ca'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = LIEDER_ROOT + 'media-lieder/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media-lieder/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-k_&x5jqt4&9=)v2n66eloas%2b48og-fr%qg$*x33r@^%2@=i'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    #'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.doc.XViewMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "lieder.apps.verdjnlib.context_processors.siteroot",
)

ROOT_URLCONF = 'lieder.settings.urls'

TEMPLATE_DIRS = (
    LIEDER_ROOT + 'templates/lieder-theme/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sites',
    'lieder.apps.misc',
    'lieder.apps.articles',
    'lieder.apps.concerts',
    'lieder.apps.documents',
    'lieder.apps.links',
    'lieder.apps.menus',
    'lieder.apps.programmes',
    'lieder.apps.singers',
)

ABSOLUTE_URL_OVERRIDES = {
    'articles.article': lambda o: '/%s/%s/' % (o.section.slug, o.slug) ,
    'articles.section': lambda o: '/%s/' % o.slug ,
    'concerts.concert': lambda o: '/concerts/%s/' % o.slug ,
    'documents.document': lambda o: '/documents/%s/%s/' % (o.category.slug, o.slug) ,
    'documents.documentcategory': lambda o: '/documents/%s/' % o.slug ,
    'links.link': lambda o: '/links/%s/%s/' % (o.category, o.slug) ,
    'links.linkcategory': lambda o: '/links/%s/' % o.slug ,
    'programmes.programme': lambda o: '/programmes/%s/' % o.slug ,
}

# LOCALE_PATHS = ( '/home/jordif/devel/djangos/locale/', )
LANGUAGES = (
    ('ca', 'Català'),
    ('es', 'Castellano'),
    ('en', 'English'),
    ('fr', 'Français'),
)
MARKUP = 'docutils'     # 'docutils', 'markdown' or 'textile'
INTERNAL_IPS = ('127.0.0.1',)
