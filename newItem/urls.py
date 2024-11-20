from django.urls import path
from .views import CadastroNovoCarro, Detalhes

app_name = 'carro'

urlpatterns = [
    path('novo_carro/', CadastroNovoCarro, name="novo_carro"),
    path('detalhes/<uuid:id>/', Detalhes, name='detalhes')
]
