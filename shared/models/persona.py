from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    app = models.CharField('Apellido Paterno', max_length=100)
    apm = models.CharField('Apellido Materno', max_length=100)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre
