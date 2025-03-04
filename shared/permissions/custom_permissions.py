from rest_framework.permissions import BasePermission
from app.usuarios.models import Usuario


class IsAdmin(BasePermission):
    def has_permission(self, request: Usuario, view):
        return request.user.is_authenticated and request.is_admin


class IsAssistant(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == "ayudante"


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ["GET", "HEAD", "OPTIONS"]
