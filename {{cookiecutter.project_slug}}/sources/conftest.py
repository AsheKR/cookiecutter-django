import pytest

from app.users.models import User
from app.users.tests.factories import UserFactory


@pytest.fixture
def user() -> User:
    return UserFactory()
