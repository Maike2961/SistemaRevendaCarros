from django.contrib import admin
from .models import Marca, Carro


admin.site.register(Marca)

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'chassi', 'cor', 'preco', 'tipo_combustivel', 'imagem', 'ano')

# Register your models here.
