from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class CategoriaProducto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    categoria = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.categoria
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=30, null=False)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField()
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, upload_to='productos/')
    en_oferta = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class ProductoOferta(models.Model):
    producto = models.OneToOneField(Producto, primary_key=True, on_delete=models.CASCADE)
    precio_oferta = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} - Precio de oferta: {self.precio_oferta}"
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.usuario} - {self.creado_en}"
    
class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def precio_total(self):
        return self.cantidad * self.precio
    
# COMUNA
# CIUDAD
