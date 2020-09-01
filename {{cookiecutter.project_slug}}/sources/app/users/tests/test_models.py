from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class TestUserModel(TestCase):
    def test_user_get_absolute_url(self, user: User):
        assert user.get_absolute_url() == f"/users/{user.username}/"
