from django.contrib.auth import authenticate
from django.test import TestCase, override_settings


class TestAdminBackend(TestCase):
    @override_settings(
        AUTHENTICATION_BACKENDS=[
            "utils.backend.admin_backend.SettingsBackend",
            "django.contrib.auth.backends.ModelBackend",
        ],
        ADMIN_LOGIN="admin",
        ADMIN_PASSWORD="admin",
    )
    def test_local_settings_admin_login(self):
        user = authenticate(username="admin", password="admin")
        self.assertIsNotNone(user, "The user must be returned.")
        self.assertIsNotNone(
            user.is_superuser, "User must have is_superuser permission"
        )
        self.assertIsNotNone(user.is_staff, "User must have is_staff permission")
