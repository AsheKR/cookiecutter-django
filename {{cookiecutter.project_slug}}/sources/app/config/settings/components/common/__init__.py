# flake8: noqa
from config.settings.components.common.app import *
from config.settings.components.common.asset import *
from config.settings.components.common.authentication import *
from config.settings.components.common.cache import *
from config.settings.components.common.environ import *
from config.settings.components.common.i18n import *
from config.settings.components.common.middleware import *
from config.settings.components.common.password import *
{% if cookiecutter.use_drf == "y" %}
from config.settings.components.common.rest_framework import *
{% endif %}
from config.settings.components.common.security import *
from config.settings.components.common.template import *
from config.settings.components.common.timezone import *
from config.settings.components.common.wsgi import *
