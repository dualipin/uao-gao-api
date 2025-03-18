from rest_framework.viewsets import ModelViewSet
from .serializers import DireccionSerializers
from .models import Direccion


class DireccionViewSet(ModelViewSet):
    serializer_class = DireccionSerializers
    queryset = Direccion.objects.all()
