from django.contrib import admin

# Register your models here.
from .models import Foto,Categoria,Producto,Carrito,Cliente,Venta,Pedido,Proveedor
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Pedido)
admin.site.register(Proveedor)
admin.site.register(Foto)
