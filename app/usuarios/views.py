from rest_framework.viewsets import ModelViewSet
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Usuario.objects.filter(id=self.request.user.id)

    @action(detail=False, methods=["get"], url_path="buscar/(?P<username>[^/.]+)")
    def buscar_por_username(self, request, username=None):
        usuario = get_object_or_404(Usuario, username=username)
        serializer = self.get_serializer(usuario)
        return Response(serializer.data)
