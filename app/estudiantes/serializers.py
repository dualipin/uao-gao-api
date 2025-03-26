from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Alumno, Beca, AlumnoBeca, AlumnoDocumentosEntregados, DiaEstudio
from app.carreras.serializers import CarreraSerializer
from app.domicilios.serializers import DireccionSerializers


class AlumnoDocumentosEntregadosSerializer(ModelSerializer):
    class Meta:
        model = AlumnoDocumentosEntregados
        fields = "__all__"


class DiaEstudioSerializer(ModelSerializer):
    class Meta:
        model = DiaEstudio
        fields = ["id", "dia"]


class AlumnoSerializer(ModelSerializer):
    dias = serializers.PrimaryKeyRelatedField(
        queryset=DiaEstudio.objects.all(), many=True
    )
    documentos_entregados = AlumnoDocumentosEntregadosSerializer(read_only=True)

    def to_representation(self, instance: Alumno):
        rep = super().to_representation(instance)
        rep["carrera"] = CarreraSerializer(instance.carrera).data
        rep["direccion"] = (
            DireccionSerializers(instance.direccion).data
            if instance.direccion
            else None
        )
        rep["dias"] = DiaEstudioSerializer(instance.dias.all(), many=True).data

        return rep

    class Meta:
        model = Alumno
        fields = "__all__"


class BecaSerializer(ModelSerializer):
    class Meta:
        model = Beca
        fields = "__all__"


class AlumnoBecaSerializer(ModelSerializer):
    class Meta:
        model = AlumnoBeca
        fields = "__all__"
