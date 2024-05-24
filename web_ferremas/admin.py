from django.contrib import admin
from .models import CategoriaProducto, Producto, ProductoOferta, Carrito, CarritoItem, DetalleBoleta, Boleta

# Register your models here.
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(ProductoOferta)
admin.site.register(Carrito)
admin.site.register(CarritoItem)
admin.site.register(DetalleBoleta)
admin.site.register(Boleta)