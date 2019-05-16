from .base import *

DEBUG = True

ALLOWED_HOST = ['192.168.250.218', 'bluesage.tk']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'control',
        'USER': 'catalogo',
        'PASSWORD': 'b1u3s4g3',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# CORS_ORIGIN_WHITELIST = (
#     'localhost:8000',
# )
STATIC_URL = '/static/'
