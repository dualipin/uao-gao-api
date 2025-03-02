from django.db import models


class Persona(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Activo", blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre
