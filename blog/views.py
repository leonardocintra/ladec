from django.shortcuts import render
from .models import Autor, Artigo, Categoria


def index(request):
    artigos = Artigo.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'artigos': artigos,
        'categorias': categorias,
    }
    return render(request, 'blog.html', context)


def artigo(request, slug):
    artigo = Artigo.objects.get(slug=slug)
    categorias = Categoria.objects.all()
    context = {
        'artigo': artigo,
        'categorias': categorias,
    }
    return render(request, 'artigo.html', context)
