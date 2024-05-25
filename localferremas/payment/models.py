from django.db import models
from ferremas.models import Pedido

class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.nombre

class EstadoPago(models.Model):
    id_estado_pago = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=False)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE, null=False)
    estado_pago = models.ForeignKey(EstadoPago, on_delete=models.CASCADE, null=False)
    monto = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return f"Pago para Pedido {self.pedido.id} ({self.estado_pago.nombre})"
