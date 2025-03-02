from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from shared.models.persona import Persona
from app.carreras.models import Carrera
from utils import generar_matricula


class Alumno(Persona):
    matricula = models.CharField(max_length=20, blank=True, unique=True)
    semestre = models.IntegerField(default=1, blank=True)
    fecha_ingreso = models.DateField(auto_now=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return f"{self.matricula} - {self.nombres} {self.apellidos}"


@receiver(pre_save, sender=Alumno)
def generar_matricula_signal(sender, instance: Alumno, **kwargs):
    if not instance.matricula:
        matricula = generar_matricula()
        instance.matricula = matricula


class Beca(models.Model):
    nombre = models.CharField(max_length=255)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Beca"
        verbose_name_plural = "Becas"

    def __str__(self):
        return self.nombre


class AlumnoBeca(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="becas")
    beca = models.ForeignKey(Beca, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now=True)
    fecha_fin = models.DateField()
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Alumno Beca"
        verbose_name_plural = "Alumnos Becas"

    def __str__(self):
        return f"{self.alumno} - {self.beca} - {self.fecha_inicio} - {self.fecha_fin}"
