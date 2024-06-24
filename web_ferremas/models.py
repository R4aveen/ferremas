from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from django.core.exceptions import ValidationError

# Create your models here.
class CategoriaProducto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    categoria = models.CharField(max_length=30,blank=False, null=False)

    def clean(self):
        if not self.categoria:
            raise ValidationError('El campo "categoria" no puede estar vacío.')

    def __str__(self):
        return self.categoria
    
class TipoProducto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    tipo = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.tipo
    
    def clean(self):
        if not self.tipo:
            raise ValidationError('El campo "tipo" no puede estar vacío.')
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=30, null=False)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField()
    categoria = models.ManyToManyField(CategoriaProducto)
    tipo = models.ManyToManyField(TipoProducto)
    imagen = models.ImageField(null=True, upload_to='productos/')
    en_oferta = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
    def clean(self):
        if not self.nombre:
            raise ValidationError('El campo "nombre" no puede estar vacío.')
        if self.precio <= 0:
            raise ValidationError('El precio debe ser mayor que cero.')
        if self.stock < 0:
            raise ValidationError('El stock no puede ser negativo.')
    
class ProductoOferta(models.Model):
    producto = models.OneToOneField(Producto, primary_key=True, on_delete=models.CASCADE)
    precio_oferta = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} - Precio de oferta: {self.precio_oferta}"
    
    def clean(self):
        if not self.producto:
            raise ValidationError('Debe especificar un producto para crear una oferta.')
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)
    pedido_aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario} - {self.creado_en}"
    
    def clean(self):
        if not self.usuario:
            raise ValidationError('Debe especificar un usuario para crear un carrito.')
            
    
class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def precio_total(self):
        return self.cantidad * self.precio
    
    def clean(self):
        if not self.carrito:
            raise ValidationError('Debe especificar un carrito para crear un carrito item.')
        if not self.producto:
            raise ValidationError('Debe especificar un producto para crear un carrito item.')
        if self.cantidad <= 0:
            raise ValidationError('La cantidad debe ser mayor que cero para crear un carrito item.')
        if self.precio <= 0:
            raise ValidationError('El precio debe ser mayor que cero para crear un carrito item.')
    
class Pedido(models.Model):
    ESTADO_PEDIDO = [
        ('pendiente', 'Pendiente'),
        ('pendiente de pago', 'Pendiente de pago'),
        ('aprobado', 'Aprobado'),
        ('preparando', 'Preparando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_PEDIDO, default='pendiente')
    creado_en = models.DateTimeField(default=timezone.now)
    actualizado_en = models.DateTimeField(auto_now=True)
    direccion_envio = models.CharField(max_length=255, null=True, blank=True)
    metodo_pago = models.CharField(max_length=50, null=True, blank=True)
    payment_token = models.UUIDField(default=uuid.uuid4, editable=False)  # Sin unique=True
    
    def __str__(self):
        return f"Pedido {self.id} - {self.usuario} - {self.estado}"

# DetallePedido (Existing model)
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.pedido.id} - Producto {self.producto.nombre} - Cantidad {self.cantidad}"



class Boleta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    total = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

class DetalleBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mensaje = models.TextField()

    def __str__(self):
        return f"Nombre: {self.nombre} | Email: {self.email}"