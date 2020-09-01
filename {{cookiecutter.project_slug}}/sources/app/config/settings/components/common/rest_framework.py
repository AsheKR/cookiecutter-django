# flake8: noqa
{%- if cookiecutter.use_drf == "y" %}
from .app import INSTALLED_APPS
from .middleware import MIDDLEWARE

INSTALLED_APPS += [
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE += [
    "corsheaders.middleware.CorsMiddleware",
]

# https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"
{%- endif %}
