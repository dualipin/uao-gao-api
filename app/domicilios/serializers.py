from rest_framework import serializers
from .models import Direccion


class DireccionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = "__all__"
