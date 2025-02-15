from django.db import models
from app.carreras.models import Carrera


class Materia(models.Model):
    clave = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    creditos = models.PositiveSmallIntegerField()
    semestre = models.PositiveSmallIntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

