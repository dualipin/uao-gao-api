# Generated by Django 5.1.6 on 2025-03-18 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0017_alumno_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaEstudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='dias',
            field=models.ManyToManyField(blank=True, related_name='alumnos', to='estudiantes.diaestudio'),
        ),
        migrations.DeleteModel(
            name='AlumnoDia',
        ),
    ]
