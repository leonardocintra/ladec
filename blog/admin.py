from django.contrib import admin

from .models import Artigo, Autor

class ArtigoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo', )}

admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Autor)
