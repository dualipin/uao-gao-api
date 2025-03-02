from rest_framework.serializers import ModelSerializer
from .models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        # fields = (
        #     "username",
        #     "nombres",
        #     "apellidos",
        #     "correo",
        #     "telefono",
        #     "is_admin",
        #     "is_active",
        # )
