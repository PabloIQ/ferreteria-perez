from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from core.models import Categoria, Foto, Producto
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.contrib.auth.decorators import login_required

# Create your views here.
def Index (request):

    return render(request, 'layout/layout.html')

def CrearProducto (request):
    return render (request, 'producto/crear.html')


def NotFound (request):
    return render (request, 'producto/notfound.html')

def Inicio (request):
    

    return render (request, 'producto/inicio.html')
    
def Carrito (request):
    return render (request, 'producto/carrito.html')

def Detproducto(request):
    return render (request, 'producto/detproducto.html')


@login_required(login_url='inicio_')
def Categoria_ (request):
    if request.method == 'POST':
        nombre_cat = request.POST['nombre']
        if not str(nombre_cat).strip():
            messages.info(request, 'Ingrese el nombre de la categoría')
        else:
            try:
                categoria = Categoria(
                    nombre = nombre_cat,
                    ud_user = User.objects.get(id=request.user.id)
                )
                categoria.save()
                messages.success(request, 'Categoría creada correctamente!')
                return redirect ('inicio_')
            except:
                messages.error(request, 'Se produjo un error, vuelva a intentarlo')
    return render (request, 'administrador/categoria.html')

def Iproducto (request):
    categoria_list = Categoria.objects.values('id', 'nombre')
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        costo = request.POST['costo']
        precio_publico = request.POST['precio_publico']
        precio_mayorista = request.POST['precio_mayorista']
        stock = request.POST['stock']
        categoria = request.POST['categoria']
        imagen = request.FILES.getlist('imagen')
        promocion = request.POST.getlist('promocion')


        try:
            with transaction.atomic():
                if len(imagen) == 0:
                    foto = Foto()
                    foto.save()
                elif len(imagen) == 1:
                    foto = Foto(
                        url1 = imagen[0]
                    )
                    foto.save()
                elif len(imagen) == 2:
                    foto = Foto(
                        url1 = imagen[0],
                        url2 = imagen[1]
                    )
                    foto.save()
                elif len(imagen) == 3:
                    foto = Foto(
                        url1 = imagen[0],
                        url2 = imagen[1],
                        url3 = imagen[2]
                    )
                    foto.save()

                producto = Producto (
                    nombre = nombre,
                    descripcion = descripcion,
                    costo = costo,
                    precio_publico = precio_publico,
                    precio_mayorista = precio_mayorista,
                    stock = stock,
                    id_categoria = Categoria.objects.get(id=categoria),
                    id_foto = Foto.objects.last(),
                    promocionar = promocion[0]
                )
                producto.save()
                messages.success(request, 'Producto creado correctamente!!!')
                return redirect ('I_producto')
        except:
            messages.error(request, 'Hubu un error al crear producto, vuelva a intentarlo!!')

    return render (request, 'administrador/producto.html', {
        'categoria': categoria_list
    })


def Proveedor (request):
    return render (request, 'administrador/Proveedor.html')

def Registrarse (request):
    return render (request, 'administrador/Registrarse.html')

def Login (request):
    if request.method == 'POST':
        usuario = request.POST['nombre']
        passw = request.POST['password']
        print ('Usuario: ', usuario)
        print ('Contraseña: ', passw)

        user = authenticate(request, username=usuario, password=passw)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {request.user.first_name}!!!')
            return redirect('inicio_')
        else:
            messages.error(request, 'Usuario o contraseña inválida!!!')

    return render (request, 'login/login.html')

def Logout (request):
    #user = request.user
    logout(request)

    messages.success(request, 'Has cerrado sesión!!!')

    return redirect ('inicio_')