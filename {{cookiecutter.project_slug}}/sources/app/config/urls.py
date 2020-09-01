from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("users/", include("users.urls", namespace="users")),
              ] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

{% if cookiecutter.use_drf == 'y' %}
# API URLS
urlpatterns += [
    path("api/", include("config.api_router")),
]
{% endif %}

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        from debug_toolbar import urls as debug_toolbar_urls  # noqa

        urlpatterns = [path('__debug__/', include(debug_toolbar_urls))] + urlpatterns
