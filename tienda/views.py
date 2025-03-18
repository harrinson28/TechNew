from django.shortcuts import render
from .models import CategoriaProd, Producto



def tienda (request):
    Productos = Producto.objects.all()
    return render(request,"tienda/Tienda.html",{"Productos":Productos})
# Create your views here.
