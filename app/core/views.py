from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from core.models import Categoria
from django.contrib.auth.models import User

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
<<<<<<< HEAD
    categoria_list = Categoria.objects.values('id', 'nombre')
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        costo = request.POST['costo']
        precio_publico = request.POST['precio_publico']
        precio_mayorista = request.POST['precio_mayorista']
        stock = request.POST['stock']
        categoria = request.POST['categoria']
        imagen = request.FILES.get('imagen')
        promocion = request.POST.getlist('promocion')

        print('Nombre: ', nombre)
        print('Descripcion: ', descripcion)
        print('Costo: ', costo)
        print('Precio Publico: ', precio_publico)
        print('Precio Mayorista: ', precio_mayorista)
        print('Stock: ', stock)
        print('Categoria: ', categoria)
        print('Imagen: ', imagen)
        print('Promocion: ', promocion[0])
    return render (request, 'administrador/producto.html', {
        'categoria': categoria_list
    })
=======
    return render (request, 'administrador/producto.html')

def Proveedor (request):
    return render (request, 'administrador/proveedor.html')
def Registrarse (request):
    return render (request, 'administrador/registrarse.html')
>>>>>>> eeefea768fe6f5e6aa4317aa3fb67922ae40bbbd
