from django.db import migrations, models
import uuid

def generate_unique_payment_tokens(apps, schema_editor):
    Pedido = apps.get_model('web_ferremas', 'Pedido')
    for pedido in Pedido.objects.all():
        pedido.payment_token = uuid.uuid4()
        pedido.save()

class Migration(migrations.Migration):

    dependencies = [
        ('web_ferremas', '0008_alter_pedido_estado'),  # Reemplaza '0009_pedido_payment_token_auto' con el nombre del archivo de migración anterior
    ]

    operations = [
        migrations.RunPython(generate_unique_payment_tokens),
    ]
