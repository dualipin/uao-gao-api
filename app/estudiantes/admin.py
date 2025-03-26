from django.contrib import admin
from .models import Alumno, AlumnoBeca, Beca, DiaEstudio, AlumnoDocumentosEntregados

admin.site.register([Alumno, AlumnoBeca, Beca, DiaEstudio, AlumnoDocumentosEntregados])
