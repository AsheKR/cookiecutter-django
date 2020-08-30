from os import environ

from split_settings.tools import optional, include

environ.setdefault('DJANGO_ENV', 'development')
ENV = environ['DJANGO_ENV']

base_settings = [
    'components/common/__init__.py',

    'environments/{0}.py'.format(ENV),
    optional('environments/local.py'),
]

include(*base_settings)
