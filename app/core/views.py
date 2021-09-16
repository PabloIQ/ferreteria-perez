from django.shortcuts import render

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