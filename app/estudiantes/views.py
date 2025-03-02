from rest_framework.viewsets import ModelViewSet
from .serializers import AlumnoBecaSerializer, AlumnoSerializer, BecaSerializer
from .models import AlumnoBeca, Alumno, Beca


class AlumnoViewSet(ModelViewSet):
    serializer_class = AlumnoSerializer
    queryset = Alumno.objects.all()


class BecaViewSet(ModelViewSet):
    serializer_class = BecaSerializer
    queryset = Beca.objects.all()


class AlumnoBecaViewSet(ModelViewSet):
    serializer_class = AlumnoBecaSerializer
    queryset = AlumnoBeca.objects.all()
