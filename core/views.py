from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from core.forms import RegistrarForm
from core.models import Categoria, Foto, Producto, Proveedor, Cliente, Carrito, Carrito_detalle
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.contrib.auth.decorators import login_required

from core.forms import RegistrarForm

# Create your views here.
def Index (request):

    return render(request, 'layout/layout.html')

def CrearProducto (request):
    return render (request, 'producto/crear.html')


def NotFound (request):
    return render (request, 'producto/notfound.html')

def Inicio (request):

    return render (request, 'producto/inicio.html')
    
def Carrito_ (request):
    carrito = ''
    subtotal = 0
    if request.user.is_authenticated:
        id_usuario = request.user.id
        id_carrito = Carrito.objects.get(id_user=id_usuario)
        carrito = Carrito_detalle.objects.filter(id_carrito=id_carrito)
        for items in carrito:
            total = float(items.total)
            subtotal += total

    return render (request, 'producto/carrito.html', {
        'carrito': carrito,
        'subtotal': subtotal
    })

def DeleteCarrito(request, id):
    fila = Carrito_detalle.objects.get(id=id)
    fila.delete()
    messages.info(request, 'Producto eleminado de la lista')
    return redirect('carrito_')

def ModificarCarrito(request, id, cantidad):
    carrito = Carrito_detalle.objects.get(id_producto=id)
    if int(cantidad) > int(carrito.id_producto.stock):
        messages.warning(request, f'Stock del producto insuficiente, solo hay {carrito.id_producto.stock} en existencia')
    else:
        total = float(carrito.precio) * float(cantidad)
        carrito.cantidad = cantidad
        carrito.total = total
        carrito.save()
        print('Producto seleccionado: ', carrito.id_producto.nombre)
        print('Id producto: ', id)
        print('Cantidad producto: ', cantidad)

    return redirect('carrito_')

def ActualizarCarrito(request, id=0, precio=0):
    if request.user.is_authenticated:
        id_usuario = request.user.id
        estado = Carrito_detalle.objects.filter(id_producto=id).filter(estado='pendiente')
        print('EStado producto: ', len(estado))

        if len(estado) == 1:
            messages.info(request, 'El producto ya existe en carrito!')
        else:
            det_carrito = Carrito_detalle(
                id_carrito = Carrito.objects.get(id_user=id_usuario),
                id_producto = Producto.objects.get(id=id),
                cantidad = 1,
                precio = precio,
                total = precio,
                estado = 'pendiente'
            )
            det_carrito.save()
            return redirect('carrito_')
    else:
        messages.info(request, 'Inicia sesion!')
    
    return redirect('contproducto_')

def Detproducto(request, id=0):
    print ('Id de producto: ', id)
    producto = Producto.objects.get(id=id)
    return render (request, 'producto/detproducto.html', {
        'producto': producto
    })

def Contproducto(request):
    producto = Producto.objects.all()

    return render (request, 'producto/contproducto.html', {
        'producto': producto
    })


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


def Proveedor_ (request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        empresa = request.POST['empresa']
        nit = request.POST['nit']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        direccion = request.POST['direccion']
        try:
            proveedor = Proveedor (
                nombre = nombre,
                empresa = empresa,
                nit = nit,
                telefono = telefono,
                correo = correo,
                dereccion = direccion
            )
            proveedor.save()
            messages.success(request, 'Se ha registrado un nuevo proveedor')
            return redirect('proveedor_')
        except:
            messages.error(request, 'Hubo un error al registrar nuevo proveedor!')

    return render (request, 'administrador/Proveedor.html')

def Registrarse (request):
    registrar_usuario = RegistrarForm()
    if request.method == 'POST':
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        nit = request.POST['nit']
        registrar_usuario = RegistrarForm(request.POST)
        
        try:
            with transaction.atomic():
                if registrar_usuario.is_valid():
                    registrar_usuario.save()
                
                cliente = Cliente(
                    user_cliente = User.objects.last(),
                    direccion = direccion,
                    telefono = telefono,
                    nit = nit,
                    tipo = 'minorista'
                )
                cliente.save()

                carrito = Carrito(
                    id_user = User.objects.last()
                )
                carrito.save()

                messages.success(request, 'Te has registrado correctamente')
                return redirect('login')
        except:
            messages.error(request, 'Hubo un error al registrarse, vuelve a intentarlo!')

    return render (request, 'administrador/Registrarse.html', {
        'registrar': registrar_usuario
    })

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