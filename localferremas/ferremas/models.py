from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ['usuario', 'producto']


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    productos = models.ManyToManyField('Producto', through='DetallePedido')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido #{self.pk} - Usuario: {self.usuario.username} - Total: {self.total}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido #{self.pedido.pk} - Producto: {self.producto.nombre} - Cantidad: {self.cantidad}"