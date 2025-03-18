from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedidos , LineaPedido
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


# Create your views here.


@login_required(login_url="/Autenticacion/iniciar_sesion")
def procesar_pedido(request):
    pedido = Pedidos.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedidos = []

    for key, value in carro.carro.items():
        lineas_pedidos.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))

    # Guardar todas las líneas de pedido en la base de datos
    LineaPedido.objects.bulk_create(lineas_pedidos)

    # Llamar a la función para enviar el correo con los datos correctos
    enviar_mail(
        pedido=pedido,
        lineas_pedidos=lineas_pedidos,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email
    )

    messages.success(request, "El pedido se ha realizado de forma correcta")
    return redirect("../tienda")

    
def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedidos.html",{
            
    "pedido":kwargs.get("pedido"),
    "lineas_pedidos": kwargs.get("lineas_pedidos"),
    "nombre":kwargs.get("nombre_usuario"),
    "email_usuario": kwargs.get("email_usuario")
    
            
    })
        
        
    mensaje_texto= strip_tags(mensaje)
    from_email="harrinsonxt28@gmail.com"
    to=kwargs.get("email_usuario")
        
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)