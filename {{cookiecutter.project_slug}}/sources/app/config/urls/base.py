from django.contrib import admin
from django.urls import path, include

from utils.doc import RedocSchemaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
]

{% if cookiecutter.use_drf == 'y' %}
v1_urlpatterns = [
    path("api/", include("config.urls.api_router")),
]

# API URLS
urlpatterns += [
    path('v1', include(v1_urlpatterns)),
    path("auth/", include('rest_framework_social_oauth2.urls')),
    path("doc/", RedocSchemaView.as_cached_view(cache_timeout=0), name="schema-redoc"),
]

{% endif %}
