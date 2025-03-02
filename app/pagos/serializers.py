from rest_framework.serializers import ModelSerializer
from .models import Pago, Concepto


class ConceptoSerializer(ModelSerializer):
    class Meta:
        model = Concepto
        fields = "__all__"


class PagoSerializer(ModelSerializer):

    class Meta:
        model = Pago
        fields = "__all__"

    def to_representation(self, instance: Pago):
        rep = super().to_representation(instance)
        rep["matricula"] = instance.alumno.matricula
        rep["alumno"] = f"{instance.alumno.nombres} {instance.alumno.apellidos}"

        rep["carrera"] = instance.alumno.carrera.nombre
        rep["concepto"] = instance.concepto.nombre
        rep["recibe"] = f"{instance.recibe.nombres} {instance.recibe.apellidos}"
        return rep
