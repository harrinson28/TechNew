from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100, required=True, label="Nombre")
    direccion = forms.CharField(max_length=255, required=True, label="Dirección")
    telefono = forms.CharField(max_length=15, required=True, label="Número de Teléfono")

    class Meta:
        model = User
        fields = [ "nombre", "direccion", "telefono", "password1", "password2"]
