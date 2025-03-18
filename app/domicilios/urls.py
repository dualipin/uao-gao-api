from rest_framework.routers import DefaultRouter
from .views import DireccionViewSet

router = DefaultRouter()
router.register(r"direcciones", DireccionViewSet)

urlpatterns = router.urls
