# Generated by Django 5.1.6 on 2025-03-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0002_alter_pago_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
