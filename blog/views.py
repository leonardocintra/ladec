from django.shortcuts import render
from .models import Autor, Artigo


def index(request):
    artigos = Artigo.objects.all()
    context = {'artigos': artigos}
    return render(request, 'blog.html', context)