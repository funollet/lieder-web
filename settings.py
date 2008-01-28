# -*- coding: utf-8 -*-
# Django settings for lieder project.

from settings_local import *

TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'ca'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_ROOT + 'media-lieder/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media-lieder/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

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
    "verdjnlib.context_processors.siteroot",
)

TEMPLATE_DIRS = (
    PROJECT_ROOT + 'templates/lieder-theme/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sites',
    'misc',
    'articles',
    'concerts',
    'documents',
    'links',
    'menus',
    'programmes',
    'singers',
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
