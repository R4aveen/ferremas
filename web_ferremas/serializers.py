from .models import *
from rest_framework import serializers

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    tipo = TipoProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'


class ProductoOfertaSerializer(serializers.ModelSerializer):
    tipo = ProductoSerializer(read_only=True)

    class Meta:
        model = ProductoOferta
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class CarritoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoItem
        fields = '__all__'
    

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'  

class DetalleBoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleBoleta
        fields = '__all__'     

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'     

