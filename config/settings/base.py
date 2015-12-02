"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import sys
import structlog
from os.path import join, abspath, dirname
from datetime import timedelta

from config.structlog_lib.logging import KeyValueRenderer

STAGE = "base"

here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here('..')
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'supa-secret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*',]

ADMINS = (
    ('Komu Wairagu', 'komuw05@gmail.com'),
)

# Application definition
DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = ('gunicorn',)

LOCAL_APPS = ( 'apps.some_app',)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

#use sqlite instead
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = root('..', 'static/') #root('static/')
STATIC_URL = '/static/'


MEDIA_ROOT = root('..', 'media/') #root('media/')
MEDIA_URL = '/media/'

# this should be a tuple.
TEMPLATE_DIRS = (
    root('..', 'templates'),
    )

# structlog logging
structlog.configure(
    logger_factory=structlog.stdlib.LoggerFactory(),
    processors=[
        structlog.processors.UnicodeEncoder(),
        KeyValueRenderer(),
    ]
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # 'sentry': {
        #     'level': 'ERROR',
        #     'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        # },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s module=%(module)s, '
            'process_id=%(process)d, %(message)s'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'celery': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'apps': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
