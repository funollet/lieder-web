"""
Splited from settings.py to keep sensible data out of SVN. Also
useful for parameters that we want customized on every deployment.
"""

PROJECT_ROOT = '/home/jordif/code/lieder/'
ROOT_URLCONF = 'urls'
SITE_URL = 'http://localhost:8000'  # required by verdjnlib.context_processors

DEBUG = True
TEMPLATE_DEBUG = True
LOCAL_DEV = True

ADMINS = (
    ('Jordi Funollet', 'jordi.f@ati.es'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3' # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = PROJECT_ROOT + 'lieder.sqlt'   # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-k_&x5jqt4&9=)v2n66eloas%2b48og-fr%qg$*x33r@^%2@=i'
