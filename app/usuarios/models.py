from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from shared.models.persona import Persona


class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario")
        if not password:
            raise ValueError("El usuario debe tener una contraseña")
        usuario = self.model(username=username, **extra_fields)
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, password, **extra_fields)


class Usuario(AbstractBaseUser, Persona, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nombres"]

    def __str__(self):
        return f"{self.username} - {self.nombres} {self.apellido_paterno} {self.apellido_materno}"
