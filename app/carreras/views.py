from rest_framework.viewsets import ModelViewSet
from .serializers import CarreraSerializer
from .models import Carrera


class CarreraViewSet(ModelViewSet):
    serializer_class = CarreraSerializer
    queryset = Carrera.objects.all()
