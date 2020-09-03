from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
]

{ % if cookiecutter.use_drf == 'y' %}
# API URLS
urlpatterns += [
    path("api/", include("config.api_router")),
    path("auth/", include('rest_framework_social_oauth2.urls')),
]
{ % endif %}
