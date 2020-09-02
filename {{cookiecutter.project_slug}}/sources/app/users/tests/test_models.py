from django.contrib.auth import get_user_model

User = get_user_model()


class TestUserModel:
    def test_user_get_absolute_url(self, user: User):
        assert user.get_absolute_url() == f"/users/{user.username}/"
