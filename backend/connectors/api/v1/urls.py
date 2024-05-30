from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135620ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135620", Testconnectors135620ViewSet, basename="testconnectors135620"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
