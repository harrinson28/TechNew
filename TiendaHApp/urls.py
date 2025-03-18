from django.urls import path
from TiendaHApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("home/",views.home, name="home"),
    path("Bienvenido/",views.bienvenido, name="Bienvenido"),
    

]

urlpatterns+=static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)