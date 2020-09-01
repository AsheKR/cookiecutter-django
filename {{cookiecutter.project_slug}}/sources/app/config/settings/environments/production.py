# flake8: noqa
from config.settings.components.common.app import INSTALLED_APPS
from config.settings.components.common.environ import env
from config.settings.components.security import *

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
{% if cookiecutter.database == 'postgres' %}
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
DATABASES['default']['PORT'] = env('DATABASE_PORT')
DATABASES['default']['USER'] = env('DATABASE_USER')
DATABASES['default']['PASSWORD'] = env('DATABASE_PASSWORD')
{% else %}
DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
{% endif %}
DATABASES['default']['ATOMIC_REQUESTS'] = True


{% if cookiecutter.cloud_provider != 'None' %}
# STORAGES
# ------------------------------------------------------------------------------
# https://django-storages.readthedocs.io/en/latest/#installation
INSTALLED_APPS += ["storages"]
{% endif %}
{% if cookiecutter.cloud_provider == 'AWS' %}
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_QUERYSTRING_AUTH = False
# DO NOT change these unless you know what you're doing.
_AWS_EXPIRY = 60 * 60 * 24 * 7
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"
}
#  https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_DEFAULT_ACL = None
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", default=None)
{% elif cookiecutter.cloud_provider == 'GCP' %}
GS_BUCKET_NAME = env("DJANGO_GCP_STORAGE_BUCKET_NAME")
GS_DEFAULT_ACL = "publicRead"
{% endif %}

{% if cookiecutter.cloud_provider != 'None' %}
# STATIC
# ------------------------
{% if cookiecutter.cloud_provider == 'AWS' %}
STATICFILES_STORAGE = "utils.storages.StaticRootS3Boto3Storage"
COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
STATIC_URL = f"https://{aws_s3_domain}/static/"
{% elif cookiecutter.cloud_provider == 'GCP' %}
STATICFILES_STORAGE = "utils.storages.StaticRootGoogleCloudStorage"
COLLECTFAST_STRATEGY = "collectfast.strategies.gcloud.GoogleCloudStrategy"
STATIC_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/static/"
{% endif %}

# MEDIA
# ------------------------------------------------------------------------------
{% if cookiecutter.cloud_provider == 'AWS' %}
DEFAULT_FILE_STORAGE = "utils.storages.MediaRootS3Boto3Storage"
MEDIA_URL = f"https://{aws_s3_domain}/media/"
{% elif cookiecutter.cloud_provider == 'GCP' %}
DEFAULT_FILE_STORAGE = "utils.storages.MediaRootGoogleCloudStorage"
MEDIA_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/media/"
{% endif %}
{% endif %}
