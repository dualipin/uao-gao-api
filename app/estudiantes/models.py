from shared.models.persona import Persona
from app.carreras.models import Carrera
from django.db import models


class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    colonia = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cp = models.CharField(max_length=5)

    def __str__(self):
        return self.calle


class Estudiante(Persona):
    matricula = models.CharField(max_length=20, unique=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    tipo_sangre = models.CharField(max_length=5, blank=True, null=True)
    domicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.matricula} {self.nombre}"
