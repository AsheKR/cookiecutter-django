from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

User = get_user_model()


class TestUserDrfUrls(TestCase):
    def test_user_detail(self, user: User):
        assert (
            reverse("api:user-detail", kwargs={"username": user.username})
            == f"/api/users/{user.username}/"
        )
        assert resolve(f"/api/users/{user.username}/").view_name == "api:user-detail"

    def test_user_list(self):
        assert reverse("api:user-list") == "/api/users/"
        assert resolve("/api/users/").view_name == "api:user-list"

    def test_user_me(self):
        assert reverse("api:user-me") == "/api/users/me/"
        assert resolve("/api/users/me/").view_name == "api:user-me"
