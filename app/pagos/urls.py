from rest_framework.routers import DefaultRouter
from .views import PagoViewSet, ConceptoViewSet

router = DefaultRouter()
router.register(r"pagos", PagoViewSet)
router.register(r"conceptos", ConceptoViewSet)

urlpatterns = router.urls
