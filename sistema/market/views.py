from django.shortcuts import render, redirect, get_object_or_404
from django.http import  HttpResponse
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages #Este módulo es para enviar mensajes flash a los usuarios
# Create your views here.
# def inicio(request):
#     return HttpResponse("<h1>Holaaa</h1>")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def inicio(request):
    return render(request, "paginas/inicio.html")

def market(request):
    market = Producto.objects.all()
    return render(request, "market/index.html", {"market": market})

def eliminar(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect('market')

def crear(request):
    formulario = ProductoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("market") 
    return render(request, "market/crear.html", {'formulario':formulario})

def prestar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if producto.stock > 0:
        producto.stock -= 1
        producto.save()
        messages.success(request, f"Se prestó un ejemplar de {producto.titulo}, quedan {producto.stock} disponibles.")
    else:
        messages.error(request, f"No hay ejemplares disponibles para el préstamo de este título: {producto.titulo}.")
    return redirect('market')
   







