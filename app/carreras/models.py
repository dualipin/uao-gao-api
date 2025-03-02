from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.FloatField(default=3.5, blank=True, max_length=4)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
