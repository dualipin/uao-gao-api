from rest_framework.routers import DefaultRouter
from .views import AlumnoBecaViewSet, BecaViewSet, AlumnoViewSet

router = DefaultRouter()
router.register(r"alumnos", AlumnoViewSet)
router.register(r"becas", BecaViewSet)
router.register(r"alumnos-becas", AlumnoBecaViewSet)

urlpatterns = router.urls
