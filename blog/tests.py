from django.test import TestCase
from blog.models import Categoria

class BlogTestCase(TestCase):
    def setUp(self):
        Categoria.objects.create(descricao="Politica")
        Categoria.objects.create(descricao="Mundo")
        Categoria.objects.create(descricao="Ciencia")

    def test_criacao_categoria(self):
        cat = Categoria.objects.get(descricao="Politica")
        self.assertEqual(cat.descricao, "Politica")
