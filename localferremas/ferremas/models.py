from django.db import models

class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=25)
    stock_inicial = models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        if not self.pk:  # Nuevo producto
            self.stock = self.stock_inicial
        super().save(*args, **kwargs)


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=250)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)
    en_oferta = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class ProductoOferta(models.Model):
    producto = models.OneToOneField(Producto, primary_key=True, on_delete=models.CASCADE)
    precio_oferta = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} - Precio de oferta: {self.precio_oferta}"
