from config.settings.components.security import *

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

SECRET_KEY = "DJANGO_SECRET_KEY"  # flake8: noqa

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'localhost',
]

# https://docs.djangoproject.com/en/dev/ref/databases/#connecting-to-the-database
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}
