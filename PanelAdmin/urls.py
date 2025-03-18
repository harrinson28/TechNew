from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('usuarios/', views.administracion_users, name='administracion_users'),
    path('productos/', views.administracion_productos, name='administracion_productos'),
    path('pedidos/', views.administracion_pedidos, name='administracion_pedidos'),
]
