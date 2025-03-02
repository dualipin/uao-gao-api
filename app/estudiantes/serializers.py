from rest_framework.serializers import ModelSerializer
from .models import Alumno, Beca, AlumnoBeca
from utils import generar_matricula


class AlumnoSerializer(ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"

        def to_representation(self, instance: Alumno):
            rep = super().to_representation(instance)
            rep["carrera"] = instance.carrera.nombre
            rep["becas"] = AlumnoBecaSerializer(instance.becas, many=True).data
            return rep

        # read_only_fields = ["matricula"]

    # def create(self, validated_data):
    #     if "matricula" not in validated_data:
    #         validated_data["matricula"] = generar_matricula()

    #     return super().create(validated_data)


class BecaSerializer(ModelSerializer):
    class Meta:
        model = Beca
        fields = "__all__"


class AlumnoBecaSerializer(ModelSerializer):
    class Meta:
        model = AlumnoBeca
        fields = "__all__"
