from django.db import models
from django.conf import settings
from django.urls import reverse


class Categoria(models.Model):
    descricao = models.CharField('Descrição', max_length=100, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


class Autor(models.Model):
    nome = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_exibir = models.CharField(
        'Nome', max_length=200, blank=False, null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nome_exibir']

    def __str__(self):
        return self.nome_exibir


class Artigo(models.Model):
    titulo = models.CharField('Título', max_length=100)
    manchete = models.CharField('Manchete', max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
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

    def get_absolute_url(self):
        return reverse('blog:artigo', kwargs={'slug': self.slug})
