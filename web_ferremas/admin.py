from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(ProductoOferta)
admin.site.register(Carrito)
admin.site.register(CarritoItem)
admin.site.register(DetalleBoleta)
admin.site.register(Boleta)
admin.site.register(TipoProducto)
admin.site.register(DetallePedido)
admin.site.register(Pedido)
admin.site.register(Contacto)