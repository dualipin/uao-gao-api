from django.contrib import admin
from .models import Alumno, AlumnoBeca, Beca

admin.site.register([Alumno, AlumnoBeca, Beca])
