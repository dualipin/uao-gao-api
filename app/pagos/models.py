from django.db import models
from app.estudiantes.models import Estudiante


class Tabulador(models.Model):
    concepto = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.concepto} - {self.monto}'


class Pago(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    conceptos = models.ManyToManyField(Tabulador)
    cliente = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.estudiante.nombre} - {self.monto}'
