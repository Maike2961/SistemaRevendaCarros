from django.urls import path
from .views import CadastroNovoCarro

app_name = 'carro'

urlpatterns = [
    path('novo_carro/', CadastroNovoCarro, name="novo_carro")
]
