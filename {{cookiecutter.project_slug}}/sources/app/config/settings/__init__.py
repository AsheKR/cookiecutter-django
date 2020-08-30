# pylint: disable=import-error
# flake8: noqa

from .app import *
from .asset import *
from .database import *
from .i18n import *
from .middleware import *
from .password import *
from .security import *
from .template import *
from .timezone import *
from .wsgi import *


DEBUG = True
SECRET_KEY = 'for-test-secret-key'
ALLOWED_HOSTS = []
