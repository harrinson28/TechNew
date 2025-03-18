from django.shortcuts import render
from django.shortcuts import render , HttpResponse 
from carro.carro import Carro

# Create your views here.




def home (request):
    
    carro=Carro(request)
    return render(request,"TiendaHApp/Home.html")

def bienvenido (request):
    return render(request,"TiendaHApp/bienvenido.html")



