from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm  # 🔹 Importado correctamente
from .forms import RegistroForm  # 🔹 Importamos nuestro formulario de registro personalizado

class VRegistro(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)  # No guardar aún en la base de datos
            usuario.first_name = form.cleaned_data["nombre"]  # Guardar el nombre
            usuario.save()  # Guardar usuario
            login(request, usuario)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {"form": form})

def cerrar_sesion(request):
    logout(request)
    return redirect("home")

def loggear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)  # 🔹 Ya no da error
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect("home")
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")

    form = AuthenticationForm()  # 🔹 Se crea correctamente el formulario
    return render(request, "login/login.html", {"form": form})
