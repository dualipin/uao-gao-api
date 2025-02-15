from shared.models.persona import Persona
from django.db import models


class Docente(Persona):
    rfc = models.CharField(max_length=20, unique=True)
    clave = models.CharField(max_length=20, unique=True)
    grado = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"{self.rfc} {self.abreviatura.upper()}. {self.nombre.upper()} {self.apellido_paterno.upper()} {self.apellido_materno.upper()}"
