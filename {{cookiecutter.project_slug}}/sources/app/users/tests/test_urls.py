import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

User = get_user_model()

pytestmark = pytest.mark.django_db


class TestUserUrls(TestCase):
    def test_detail(self, user: User):
        assert (
            reverse("users:detail", kwargs={"username": user.username})
            == f"/users/{user.username}/"
        )
        assert resolve(f"/users/{user.username}/").view_name == "users:detail"

    def test_update(self):
        assert reverse("users:update") == "/users/~update/"
        assert resolve("/users/~update/").view_name == "users:update"

    def test_redirect(self):
        assert reverse("users:redirect") == "/users/~redirect/"
        assert resolve("/users/~redirect/").view_name == "users:redirect"


