from rest_framework.routers import DefaultRouter

from manual.views import ManualViewSet

router = DefaultRouter()
router.register(r"manual", ManualViewSet, basename="manual")

urlpatterns = router.urls
