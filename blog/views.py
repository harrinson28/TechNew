from django.shortcuts import render
from blog.models import  post, Categoria

# Create your views here.

def blog (request):
    posts = post.objects.all()
    return render(request,"blog/Blog.html",{"posts":posts})


def categoria(request,categoria_id):
    categoria= Categoria.objects.get(id=categoria_id)
    posts =post.objects.filter(categorias=categoria) 
    return render(request,"blog/categorias.html",{"categoria":categoria,"posts":posts})
