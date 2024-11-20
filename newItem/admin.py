from django.contrib import admin
from .models import Marca, Carro


admin.site.register(Marca)

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca_carro', 'chassi', 'cor', 'preco', 'tipo_combustivel', 'imagem', 'ano', 'criado_por')

# Register your models here.
