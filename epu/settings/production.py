import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ecologicalpartyofuganda.com', 'www.ecologicalpartyofuganda.com', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('SQL_DATABASE', os.getenv('DB_NAME')),
        'USER': os.environ.get('SQL_USER', os.getenv('DB_USER')),
        'PASSWORD': os.environ.get('SQL_PASSWORD', os.getenv('DB_PASS')),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', ''),
    }
}

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
