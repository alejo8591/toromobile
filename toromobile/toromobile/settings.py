# Django settings for toromobile project.

DEBUG = True

__version__ = "0.0.1"
__status__ = "alpha"

# Get the current directory
import os
ROOT_CONF = os.path.dirname(os.path.realpath(__file__))

TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}


ADMINS = (
    ('Alejandro Romero', 'alejo8591@gmail.com'),
)

MANAGERS = ADMINS
"""
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'heroku_210e8083675e5dd',                     
            'USER': 'f4c58c2ba25df7',                     
            'PASSWORD': 'ea7dc267',                 
            'HOST': '',                     
            'PORT': '',               
            }
}
"""

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'toromobileh',                     
            'USER': 'root',                     
            'PASSWORD': '',                 
            'HOST': '',                     
            'PORT': '',               
            }
}

#django debug toolbar
INTERNAL_IPS = ('127.0.0.1',)
TIME_ZONE = 'America/Bogota'
LANGUAGE_CODE = 'es-ES'
LANGUAGES = (
    ('es_ES', 'Espanol'),
    ('en_GB', 'English'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ROOT_CONF
MEDIA_URL = '/uploads/'
STATIC_ROOT = ROOT_CONF + '/static/'
STATIC_URL = '/static'
ADMIN_MEDIA_PREFIX = STATIC_URL + '/grappelli/'
# Additional locations of static files
STATICFILES_DIRS = (
    (ROOT_CONF + '/static_files/'),
)
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3b0iu=j40o^iwzyt7_@a5p=6%@@=gk8g&amp;+3jgw#1re7ls**(3h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'toromobile.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'toromobile.wsgi.application'

TEMPLATE_DIRS = (
    (ROOT_CONF + '/templates'),
)

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

GRAPPELLI_ADMIN_TITLE = "<li class='user-options-container collapse closed'> \
<a href='javascript://' class='user-options-handler collapse-handler'> \
toromobile %s</a><ul class='user-options'><li><a href='/' \
style='padding:10px;'>Back to site</a></li></ul></li>" % (__version__)
#GRAPPELLI_ADMIN_URL = '/admin'
#GRAPPELLI_INDEX_DASHBOARD = 'toromobile.dashboard.CustomIndexDashboard'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'devserver',
    'grappelli',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'django_extensions',
    #'debug_toolbar',
    'car',
    'city',
    'company',
    'despatch',
    'driver',
    'packet',
    'routes'
)

FIXTURE_DIRS = (
   '/Users/alejo8591/.virtualenvs/toromobile/vivid-ocean-1546/city/fixtures/',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)