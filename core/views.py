from django.shortcuts import render
from blog.models import Autor, Artigo


def index(request):
    artigos = Artigo.objects.all()
    context = {'artigos': artigos}
    return render(request, 'index.html', context)


def sobre(request):
    return render(request, 'sobre.html')
