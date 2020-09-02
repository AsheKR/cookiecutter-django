import os
import sys

import pytest
from django.contrib.auth import get_user_model

from users.tests.factories import UserFactory

sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

User = get_user_model()


@pytest.fixture(autouse=True)
def enable_db(db):
    pass


@pytest.fixture
def user() -> User:
    return UserFactory()
