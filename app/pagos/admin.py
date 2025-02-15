from django.contrib import admin
from .models import Concepto, Pago, Tabulador

admin.site.register([Concepto, Pago, Tabulador])
