# Generated by Django 5.0.4 on 2024-05-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ferremas', '0006_boleta_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='pedido_aprobado',
            field=models.BooleanField(default=False),
        ),
    ]
