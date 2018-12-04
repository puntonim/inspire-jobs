"""
Development settings.
"""

from .settings_base import *


DEBUG = True
SECRET_KEY = 'secretkey'
AUTH_PASSWORD_VALIDATORS = []
ALLOWED_HOSTS = ['*']

INSPIRE_DATABASE_KEY = 'inspirehep'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inspire-jobs',
        'USER': 'inspire-jobs',
        'PASSWORD': 'mypassword',
        # 'HOST': '127.0.0.1',
        # 'PORT': '5432',
    },

    # To grant read permission to a user in PostreSQL:
    # GRANT SELECT ON ALL TABLES IN SCHEMA public TO "inspire-read-api";
    # To grant permission to create new dbs (used by Django test tools):
    # ALTER USER "inspire-read-api" CREATEDB;

    INSPIRE_DATABASE_KEY: {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inspire-prod',
        'USER': 'inspire-jobs',
        'PASSWORD': 'myotherpassword',
    }
}
