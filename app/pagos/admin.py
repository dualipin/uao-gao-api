from django.contrib import admin
from .models import Concepto, Pago


admin.site.register(
    [
        Concepto,
        Pago,
    ]
)
