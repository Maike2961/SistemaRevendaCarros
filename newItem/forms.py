from django import forms
from .models import Carro

class CadastroCarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ("nome", "chassi", "marca_carro", "cor", "preco", "tipo_combustivel", "ano", 'imagem')
        widgets = {
            "nome": forms.TextInput(attrs={
                'class': "w-full py-4 px-6 rounded-xl border"
            }),
            "chassi": forms.TextInput(attrs={
                'class': "w-full py-4 px-6 rounded-xl border"
            }),
            "marca_carro": forms.Select(attrs={
                'class': "w-full py-4 px-6 rounded-xl border"
            }),
            "cor": forms.TextInput(attrs={
                'class': "w-full py-4 px-6 rounded-xl border"
            }),
            "preco":forms.TextInput(attrs={
                'class': "w-full py-4 px-6 rounded-xl border"
            }),
            "tipo_combustivel": forms.Select(attrs={
                'class': "w-full py-4 px-6 rounded-xl border"
            }),
            "ano":forms.NumberInput(attrs={
                'class': "w-full py-4 px-6 rounded-xl border"
            }),
            "imagem":forms.FileInput(attrs={
                'class': "w-full py-4 px-6 rounded-xl border"
            }),
        }