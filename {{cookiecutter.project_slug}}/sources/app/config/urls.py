from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from debug_toolbar import urls as debug_toolbar_urls  # noqa
    from django.conf.urls.static import static  # noqa

    urlpatterns = [path('__debug__/', include(debug_toolbar_urls))] + urlpatterns + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
