from django.contrib import admin
from .models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio', 'stock', 'descripcion', 'tipo']
    search_fields = ['nombre']
    list_per_page = 10
    list_filter = ['id', 'tipo']
    list_editable = ['precio', 'stock', 'descripcion', 'tipo']
    ordering = ['id']


admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoProducto)