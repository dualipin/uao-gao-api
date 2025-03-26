from rest_framework.viewsets import ModelViewSet
from .serializers import (
    AlumnoBecaSerializer,
    AlumnoSerializer,
    BecaSerializer,
    AlumnoDocumentosEntregadosSerializer,
    DiaEstudioSerializer,
)
from .models import AlumnoBeca, Alumno, Beca, AlumnoDocumentosEntregados, DiaEstudio
from rest_framework.response import Response
from rest_framework import status


class AlumnoDocumentosEntregadosViewSet(ModelViewSet):
    serializer_class = AlumnoDocumentosEntregadosSerializer
    queryset = AlumnoDocumentosEntregados.objects.all()


class AlumnoViewSet(ModelViewSet):
    serializer_class = AlumnoSerializer
    queryset = Alumno.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        matricula = self.request.query_params.get("matricula")
        carrera = self.request.query_params.get("carrera")
        semestre = self.request.query_params.get("semestre")
        filters = {}
        if carrera:
            filters["carrera"] = carrera
        if matricula:
            filters["matricula"] = matricula
        if semestre:
            filters["semestre"] = semestre
        return qs.filter(**filters)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BecaViewSet(ModelViewSet):
    serializer_class = BecaSerializer
    queryset = Beca.objects.all()


class AlumnoBecaViewSet(ModelViewSet):
    serializer_class = AlumnoBecaSerializer
    queryset = AlumnoBeca.objects.all()

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)


class DiaViewSet(ModelViewSet):
    serializer_class = DiaEstudioSerializer
    queryset = DiaEstudio.objects.all()
