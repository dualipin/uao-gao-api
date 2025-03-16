from django.contrib import admin
from .models import Concepto, Pago


admin.site.register([Concepto])


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = (
        "folio",
        "alumno",
        "fecha",
        "monto",
        "concepto",
        "recibe",
        "creado",
        "modificado",
    )
