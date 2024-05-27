# Generated by Django 5.0.4 on 2024-05-27 03:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ferremas', '0008_alter_pedido_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='payment_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('pendiente de pago', 'Pendiente de pago'), ('aprobado', 'Aprobado'), ('preparando', 'Preparando'), ('enviado', 'Enviado'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20),
        ),
    ]