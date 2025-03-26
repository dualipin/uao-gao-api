from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from shared.models.persona import Persona
from app.carreras.models import Carrera
from utils import generar_matricula
from app.domicilios.models import Direccion


class DiaEstudio(models.Model):
    dia = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.dia


class Alumno(Persona):
    matricula = models.CharField(max_length=20, blank=True, unique=True)
    semestre = models.IntegerField(default=1, blank=True)
    fecha_ingreso = models.DateField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    dias = models.ManyToManyField(DiaEstudio, related_name="alumnos", blank=True)
    direccion = models.ForeignKey(
        Direccion,
        on_delete=models.CASCADE,
        related_name="alumnos_direccion",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return f"{self.matricula} - {self.nombres} {self.apellido_paterno} {self.apellido_materno}"


@receiver(pre_save, sender=Alumno)
def generar_matricula_signal(sender, instance: Alumno, **kwargs):
    if not instance.matricula:
        matricula = generar_matricula()
        instance.matricula = matricula


class AlumnoDocumentosEntregados(models.Model):
    alumno = models.OneToOneField(
        Alumno,
        on_delete=models.CASCADE,
        related_name="documentos_entregados",
        default=None,
    )
    acta_nacimiento = models.BooleanField(default=False)
    certificado_bachillerato = models.BooleanField(default=False)
    curp = models.BooleanField(default=False)
    certificado_medico = models.BooleanField(default=False)
    folder = models.BooleanField(default=False)


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
