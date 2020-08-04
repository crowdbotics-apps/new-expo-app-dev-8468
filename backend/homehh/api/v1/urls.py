from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GFhgjhgjhViewSet

router = DefaultRouter()
router.register("gfhgjhgjh", GFhgjhgjhViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
