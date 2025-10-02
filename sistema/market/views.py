from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import Producto
from .forms import ProductoForm
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






