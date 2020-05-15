from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('artigo/<slug:slug>/', views.artigo, name='artigo-detalhe'),
]