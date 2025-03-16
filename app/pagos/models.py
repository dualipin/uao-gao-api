from django.db import models
from app.estudiantes.models import Alumno
from app.usuarios.models import Usuario
import uuid


class Concepto(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Concepto"
        verbose_name_plural = "Conceptos"

    def __str__(self):
        return self.nombre


class Pago(models.Model):
    TIPO_PAGO = (
        ("E", "Efectivo"),
        ("T", "Transferencia"),
    )

    folio = models.AutoField(
        unique=True,
        primary_key=True,
        editable=False,
        blank=True,
    )
    cadena = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
    )
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="pagos")
    fecha = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
    recibe = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    tipo = models.CharField(max_length=1, choices=TIPO_PAGO, default="E")

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f"{self.alumno} - {self.fecha} - {self.monto}"
