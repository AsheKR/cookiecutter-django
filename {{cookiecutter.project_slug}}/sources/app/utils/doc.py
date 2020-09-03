from drf_yasg import openapi
from drf_yasg.renderers import OpenAPIRenderer, ReDocRenderer as BaseReDocRenderer
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.schemas import SchemaGenerator

BaseSchemaView = get_schema_view(
    openapi.Info(
        title='{{ cookiecutter.project_name }}',
        default_version='v1',
        contact=openapi.Contact(email='tech@ashe.kr'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=SchemaGenerator,
)


class ReDocRenderer(BaseReDocRenderer):
    template = "docs/redoc.html"


class RedocSchemaView(BaseSchemaView):
    renderer_classes = (ReDocRenderer, OpenAPIRenderer)
