# En tu archivo serializers.py dentro de tu aplicación payment

from rest_framework import serializers
from .models import Pago

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class PagoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['pedido', 'metodo_pago', 'monto', 'estado_pago', 'fecha']

class TransaccionPostSerializer(serializers.Serializer):
    pedido = serializers.IntegerField()
    cliente = serializers.IntegerField()
    pago = serializers.IntegerField()

    def create(self, validated_data):
        # Aquí puedes crear y devolver una nueva instancia de la transacción
        pass