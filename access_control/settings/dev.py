from .base import *

DEBUG = True

ALLOWED_HOST = ['192.168.100.169']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'controldb',
        'USER': 'postgres',
        'PASSWORD': 'Solecismo1',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# CORS_ORIGIN_WHITELIST = (
#     'localhost:8000',
# )
STATIC_URL = '/static/'
