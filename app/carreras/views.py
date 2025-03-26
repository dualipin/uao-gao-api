from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import CarreraSerializer
from .models import Carrera
from shared.permissions.custom_permissions import ReadOnly


class CarreraViewSet(ModelViewSet):
    serializer_class = CarreraSerializer
    queryset = Carrera.objects.all()
