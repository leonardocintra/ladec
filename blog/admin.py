from django.contrib import admin

from .models import Artigo, Autor, Categoria, ArtigoImages


class ArtigoImagemInline(admin.TabularInline):
    model = ArtigoImages
    extra = 5


class ArtigoAdmin(admin.ModelAdmin):
    admin.site.site_header = 'Grupo Ladec - Laboratórios'
    prepopulated_fields = {'slug': ('titulo', )}
    inlines = [ArtigoImagemInline]


admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Autor)
admin.site.register(Categoria)
