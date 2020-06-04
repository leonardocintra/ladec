from django.test import TestCase
from blog.models import Categoria, Autor, Artigo
from django.contrib.auth.models import User


class BlogTestCase(TestCase):
    def setUp(self):
        # User
        test_user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(
            username='testuser2', password='2HJ1vRV0Z&3iD')

        # Categoria
        Categoria.objects.create(descricao="Politica")
        Categoria.objects.create(descricao="Esporte")

        # Autor
        autor = Autor.objects.create(
            nome=User.objects.get(id=2), nome_exibir="Olavo de Carvalho")

    def test_get_categoria(self):
        cat = Categoria.objects.get(descricao="Politica")
        self.assertEqual(cat.descricao, "Politica")

    def test_categoria_descricao_max_length(self):
        categoria = Categoria.objects.get(id=1)
        max_length = categoria._meta.get_field('descricao').max_length
        self.assertEquals(max_length, 100)

    def test_criacao_categoria(self):
        """ Testa cadastro de categoria """
        cat = Categoria.objects.create(descricao="Teste_Categoria")
        self.assertEqual(cat.descricao, "Teste_Categoria")

    def test_criacao_autor(self):
        """ Testa casdastro de autor """
        autor = Autor.objects.create(
            nome=User.objects.get(id=1), nome_exibir="Maria Ronalda")
        self.assertEqual(autor.nome_exibir, "Maria Ronalda")

    def test_autor_nome_exibir_max_length(self):
        """ Testa se a quantidade de caracteres eh 200 no nome_exibir """ 
        autor = Autor.objects.get(id=1)
        max_length = autor._meta.get_field("nome_exibir").max_length
        self.assertEqual(max_length, 200)
