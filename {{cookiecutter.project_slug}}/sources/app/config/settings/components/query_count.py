from config.settings.components.common.middleware import MIDDLEWARE

MIDDLEWARE += [
    # https://github.com/bradmontgomery/django-querycount
    'querycount.middleware.QueryCountMiddleware',
]
