from rest_framework.viewsets import ModelViewSet
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=["get"], url_path="buscar/(?P<username>[^/.]+)")
    def buscar_por_username(self, request, username=None):
        usuario = get_object_or_404(Usuario, username=username)
        serializer = self.get_serializer(usuario)
        return Response(serializer.data)
