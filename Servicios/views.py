from django.shortcuts import render
from Servicios.models import Servicio

# Create your views here.
def servicios (request):
    Servicios = Servicio.objects.all()
    return render(request,"Servicios/Servicios.html",{"Servicios": Servicios})