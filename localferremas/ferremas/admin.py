from django.contrib import admin
from .models import *
# Register your models here.

class ProductoOfertaInline(admin.StackedInline):
    model = ProductoOferta
    can_delete = False
    verbose_name_plural = 'Producto en oferta'
    
class ProductoAdmin(admin.ModelAdmin):
    inlines = (ProductoOfertaInline,)
    list_display = ['id', 'nombre', 'precio', 'stock', 'descripcion', 'tipo', 'en_oferta']
    search_fields = ['nombre']
    list_per_page = 10
    list_filter = ['id', 'tipo', 'en_oferta']
    list_editable = ['precio', 'stock', 'descripcion', 'tipo', 'en_oferta']
    ordering = ['id']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        # Trae el precio en oferta y actualiza la tablas
        precio_oferta = form.cleaned_data.get('precio_oferta', obj.precio)
        
        # Revisa el precio en oferta y actualiza la lista 
        if obj.en_oferta:
            producto_oferta, created = ProductoOferta.objects.get_or_create(producto=obj)
            producto_oferta.precio_oferta = precio_oferta
            producto_oferta.save()
        else:
            try:
                producto_oferta = ProductoOferta.objects.get(producto=obj)
                producto_oferta.delete()
            except ProductoOferta.DoesNotExist:
                pass
    # Método personalizado para mostrar el tipo de producto en el admin
    def get_tipo(self, obj):
        return obj.tipo.nombre if obj.tipo else ''



admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoProducto)
admin.site.register(ProductoOferta)
admin.site.register(Carrito)