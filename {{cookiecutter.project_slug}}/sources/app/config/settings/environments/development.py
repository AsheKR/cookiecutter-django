from config.settings.components.debug_toolbar import *  # noqa

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

SECRET_KEY = "DJANGO_SECRET_KEY"  # noqa

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
    '[::1]',
]

# https://docs.djangoproject.com/en/dev/ref/databases/#connecting-to-the-database
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}
