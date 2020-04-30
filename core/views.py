from django.shortcuts import render
from blog.models import Autor, Artigo
from django.shortcuts import get_object_or_404


def index(request):
    artigos = Artigo.objects.all()
    context = {'artigos': artigos}
    return render(request, 'index.html', context)
