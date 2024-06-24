from django.contrib import admin
from .models import Corretora


@admin.register(Corretora)
class CorretoraAdmin(admin.ModelAdmin):
    list_display = ['nome_corretora', 'telefone', 'email', 'cnpj', 'pessoa_contato']
    search_fields = ['nome_corretora', 'email']
