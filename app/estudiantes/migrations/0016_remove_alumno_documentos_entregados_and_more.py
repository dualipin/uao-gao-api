# Generated by Django 5.1.6 on 2025-03-17 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0015_remove_alumnodocumentosentregados_alumno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='documentos_entregados',
        ),
        migrations.AddField(
            model_name='alumnodocumentosentregados',
            name='alumno',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='documentos_entregados', to='estudiantes.alumno'),
        ),
    ]
