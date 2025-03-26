from rest_framework.routers import DefaultRouter
from .views import (
    AlumnoBecaViewSet,
    BecaViewSet,
    AlumnoViewSet,
    AlumnoDocumentosEntregadosViewSet,
    DiaViewSet,
)

router = DefaultRouter()
router.register(r"alumnos", AlumnoViewSet)
router.register(r"becas", BecaViewSet)
router.register(r"alumnos-becas", AlumnoBecaViewSet)
router.register(r"alumnos-documentos-entregados", AlumnoDocumentosEntregadosViewSet)
router.register(r"alumnos-dias", DiaViewSet)

urlpatterns = router.urls
