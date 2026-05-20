from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserTestViewSet

router = DefaultRouter()
router.register("user-tests", UserTestViewSet, basename="user-test")

urlpatterns = [
    path("", include(router.urls)),
]
