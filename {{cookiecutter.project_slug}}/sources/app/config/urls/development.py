from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .base import urlpatterns

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        from debug_toolbar import urls as debug_toolbar_urls  # noqa

        urlpatterns += [
            path('__debug__/', include(debug_toolbar_urls)),
            *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
            *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        ]
