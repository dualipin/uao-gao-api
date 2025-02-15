from django.db import models
from app.estudiantes.models import Estudiante
from app.materias.models import Materia
from app.docentes.models import Docente


class Calificacion(models.Model):
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.estudiante} {self.materia} {self.calificacion}"
