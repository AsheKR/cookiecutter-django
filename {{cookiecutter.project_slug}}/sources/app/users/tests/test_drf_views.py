from django.contrib.auth import get_user_model
from django.test import RequestFactory

from users.apis.views import UserViewSet

User = get_user_model()


class TestUserViewSet:
    def test_get_queryset(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)

        assert response.data == {
            "username": user.username,
            "email": user.email,
            "name": user.name,
            "url": f"http://testserver/api/users/{user.username}/",
        }
