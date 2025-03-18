from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CategoriaProd(models.Model):
     nombre=models.CharField(max_length=50)
     created=models.DateTimeField(auto_now_add=True)
     updated=models.DateTimeField(auto_now_add=True)
     
     class Meta:
          verbose_name= "categoriaProd"
          verbose_name_plural="categoriasprod"
     def __str__(self):
          return self.nombre
     
     
class Producto(models.Model):
     nombre=models.CharField(max_length=50,)
     descripcion=models.CharField(max_length=500)
     precio=models.FloatField()
     imagen=models.ImageField(upload_to="tienda" ,null=True , blank=True)
     categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
     disponibilidad=models.BooleanField(default=True)
     created=models.DateTimeField(auto_now_add=True)
     updated=models.DateTimeField(auto_now_add=True)
     
     class Meta:
          verbose_name="Producto"
          verbose_name_plural="Productos"
          
    