from django.conf import settings
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import PacienteViewSet


schema_view = get_schema_view(
    openapi.Info(
        title='App Docs',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

if settings.DEBUG:
    router = SimpleRouter()
else:
    router = DefaultRouter()

router.register('paciente', PacienteViewSet, basename='paciente')

urlpatterns = [
    path(r'', include((router.urls, 'api'), namespace='api')),
    path(r'docs/', include_docs_urls(title='App Docs',
                                     authentication_classes=[],
                                     permission_classes=[])),
]
