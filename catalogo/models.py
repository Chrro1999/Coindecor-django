from django.db import models
from django.conf import settings

# Diseño de la base de datos 

# Tabla de categorías
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
# Tabla de productos
class Productos(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Hasta 10 digitos y 2 decimales
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True) # Imagen principal
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

# Nueva tabla para múltiples fotos por producto
class ImagenProducto(models.Model):
    producto = models.ForeignKey(Productos, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/galeria/')
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Imagen adicional de {self.producto.nombre}"

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente de pago'),
        ('PAGADO', 'Pagado'),
        ('EN_PROCESO', 'En Proceso'),
        ('COMPLETADO', 'Completado'),
        ('FALLIDO', 'Fallido'), # Corregido "FALLIFO"
    ]
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    nombre_completo = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100, default='Quito')

    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')

    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.nombre_completo}"
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # Usamos un bloque try/except por si el producto fue borrado (null=True)
        nombre_prod = self.producto.nombre if self.producto else "Producto eliminado"
        return f"{self.cantidad} x {nombre_prod} en Pedido {self.pedido.id}"