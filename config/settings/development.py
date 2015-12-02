from .base import *


STAGE = "development"


INSTALLED_APPS += (
    'django_extensions', 
    )


LOGGING['loggers']['django.request']['handlers'] = ['console']
LOGGING['loggers']['django.request']['level'] = 'DEBUG'
LOGGING['loggers']['celery']['level'] = 'INFO'
LOGGING['loggers']['celery']['handlers'] = ['console']
LOGGING['formatters']['verbose']['format'] += '\n'