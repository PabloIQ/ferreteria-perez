from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Foto (models.Model):
    url1 = models.ImageField(default='null', verbose_name='Miniatura', upload_to='imagenes')
    url2 = models.ImageField(default='null', verbose_name='Miniatura', upload_to='imagenes')
    url3 = models.ImageField(default='null', verbose_name='Miniatura', upload_to='imagenes')

class Categoria (models.Model):
    nombre = models.CharField(max_length=60)
    fecha_creacion = models.DateField(auto_now_add=True)
    ud_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Producto (models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=150)
    costo = models.FloatField(default=0)
    precio_publico = models.FloatField(default=0)
    precio_mayorista = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateField(auto_now_add=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_foto = models.ForeignKey(Foto, on_delete=models.CASCADE)
    promocionar = models.PositiveIntegerField(default=0)

class Visita_prod (models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_visita = models.DateField()
    no_vistas = models.PositiveIntegerField(default=0)

class Foro (models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    estrellas = models.PositiveIntegerField(default=0)
    sugerencia = models.CharField(max_length=200)
    fecha_creacion = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=60)

class Carrito (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

class Carrito_detalle (models.Model):
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.FloatField(default=0)
    total = models.FloatField(default=0)
    estado = models.CharField(max_length=10)
    
class Cliente (models.Model):
    user_cliente = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=8)
    nit = models.CharField(max_length=8)
    tipo = models.CharField(max_length=20)

class Venta (models.Model):
    fecha_creacion = models.DateField(auto_now_add=True)
    id_user = ForeignKey(User, on_delete=models.CASCADE)

class Detalle_venta (models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

class Pedido (models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado_envio = models.CharField(max_length=10)
    no_guia = models.CharField(max_length=15)

class Proveedor (models.Model):
    nombre = models.CharField(max_length=60)
    empresa = models.CharField(max_length=60)
    nit = models.CharField(max_length=8)
    telefono = models.CharField(max_length=8)
    correo = models.CharField(max_length=80)
    dereccion = models.CharField(max_length=60)

class Compra (models.Model):
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

class Detalle_compra (models.Model):
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    costo = models.FloatField(default=0)
    total = models.FloatField(default=0)