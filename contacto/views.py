from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage


# Create your views here.


def contacto (request):
    formularo_contacto = FormularioContacto()
    
    if request.method=="POST":
        formularo_contacto = FormularioContacto(data=request.POST)
        if formularo_contacto.is_valid():
            nombre =request.POST.get("nombre")
            email =request.POST.get("email")
            contenido =request.POST.get("contenido")
            
            email=EmailMessage("Mensaje de Pedidos 247",
            "el usuario {} direccion {} motivo:\n\n {}".format(nombre,email,contenido),"",["harrinsonxt28@gmail.com"],reply_to=[email])
            
            try:
                email.send()
                
                return redirect("/contacto/?valido")
                
            except:
                return redirect("/contacto/?invalido")
                
            
            
            
    return render(request,"Contacto/Contacto.html", {'miformularo':formularo_contacto})


