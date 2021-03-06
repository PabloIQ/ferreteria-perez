"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index_'),
    path('crear-producto/', views.CrearProducto, name='crear_producto'),
    path('notfound/', views.NotFound, name='not_found'),
    path('inicio/', views.Inicio, name='inicio_'),
    path('carrito/', views.Carrito_, name='carrito_'),
    path('delete-carrito/<id>', views.DeleteCarrito, name='delete_carrito'),
    path('vender/', views.Vender, name='vender'),
    path('actualizar-carrito/<id>/<precio>', views.ActualizarCarrito, name='actualizar_carrito'),
    path('modificar-carrito/<id>/<cantidad>', views.ModificarCarrito, name='modificar_carrito'),
    path('categoria/', views.Categoria_, name='categoria_'),
    path('iproducto/',views.Iproducto, name='I_producto'),
    path('proveedor/', views.Proveedor_, name='proveedor_'),
    path('registrarse/',views.Registrarse, name='registrarse_'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('detproducto/<id>',views.Detproducto, name='detproducto_'),
    path('contproducto/', views.Contproducto, name='contproducto_'),
    path('producto-categoria/<id>', views.ProductoCategoria, name='producto_categoria'),
    path('buscar-producto/<texto>', views.BuscarProducto, name='buscar_producto'),
    path('pedidos/', views.VerPedidos, name='pedidos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#Configuracion para cargar imagenes
"""if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""