from django.db import models
from django.conf import settings


class Autor(models.Model):
    nome = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_exibir = models.CharField('Nome', max_length=200, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField('Título', max_length=100)
    manchete = models.CharField('Manchete', max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    slug = models.SlugField('Identificador Google', max_length=100,
                            help_text='identificador baseado no titulo', unique=True)
    descricao = models.TextField('Descrição')
    data_publicacao = models.DateTimeField(
        'Data Publicação', auto_now_add=True)

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo
