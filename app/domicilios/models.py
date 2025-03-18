from django.db import models


# Create your models here.
class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    numero_exterior = models.CharField(max_length=10)
    numero_interior = models.CharField(max_length=10, blank=True, null=True)
    colonia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return f"{self.calle} {self.numero_exterior}, {self.colonia}, {self.municipio}, {self.estado}, {self.codigo_postal}"
