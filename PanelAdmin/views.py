from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from tienda.models import Producto 
from pedidos.models import Pedidos

@login_required

def dashboard(request):
    return render(request, 'PanelAdmin/dashboard.html')

@login_required
def administracion_users (request):
    usuarios = User.objects.all()
    return render(request,'PanelAdmin/administracion_users.html',{'usuarios':usuarios})

@login_required
def administracion_productos (request):
    productos=Producto.objects.all()
    return render(request,'PanelAdmin/administracion_productos.html',{'productos':productos})

@login_required
def administracion_pedidos (request):
    pedidos = Pedidos.objects.prefetch_related('lineapedido_set__producto')
    return render(request, 'PanelAdmin/administracion_pedidos.html', {'pedidos': pedidos})