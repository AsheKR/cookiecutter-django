from config.settings.components.common.environ import env  # noqa
from config.settings.components.security import *  # noqa

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

SECRET_KEY = env("SECRET_KEY")

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    env.str("DOMAIN_NAME"),
]

# https://docs.djangoproject.com/en/dev/ref/databases/#connecting-to-the-database
DATABASES = {'default': {'HOST': env('DATABASE_URL')}}
DATABASES['default']['NAME'] = env('DATABASE_NAME')
{% if cookiecutter.database == 'postgres' %}  # noqa
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
DATABASES['default']['PORT'] = env('DATABASE_PORT')
DATABASES['default']['USER'] = env('DATABASE_USER')
DATABASES['default']['PASSWORD'] = env('DATABASE_PASSWORD')
{%- else %}  # noqa
DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
{%- endif %}  # noqa
DATABASES['default']['ATOMIC_REQUESTS'] = True
