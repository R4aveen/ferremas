# Generated by Django 5.0.4 on 2024-05-22 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='estado_venta',
            field=models.CharField(choices=[('Exitosa', 'Exitosa'), ('Cancelada', 'Cancelada'), ('Pendiente', 'Pendiente')], default='Exitosa', max_length=100),
        ),
    ]
