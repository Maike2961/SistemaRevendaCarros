from django.db import models
from django.contrib.auth.models import User
from babel.numbers import format_currency
import uuid

class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

class Marca(Base):
    marca_carro = models.CharField(max_length=255)

    class Meta:
        ordering = ('marca_carro',)
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.marca_carro

class Carro(Base):
    GASOLINA = "Gasolina"
    HIBRIDO = "Hibrido"
    ELETRICO = "Eletrico"
    DIESEL = "Diesel"

    TIPO_COMBUSTIVEL = [
        (GASOLINA, 'Gasolina'), (DIESEL, 'Diesel'), (ELETRICO, 'Elétrico'), (HIBRIDO, 'Híbrido'),
    ]
    
    nome = models.CharField("Nome", max_length=255)
    chassi = models.CharField("Chassi", unique=True, max_length=255)
    marca_carro = models.ForeignKey(Marca, related_name="items", on_delete=models.CASCADE)
    cor = models.CharField("Cor", max_length=15)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_por = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)
    tipo_combustivel = models.CharField(choices=TIPO_COMBUSTIVEL, max_length=20, default="GASOLINA")
    ano = models.IntegerField()
    imagem = models.ImageField(upload_to="media")

    def __str__(self):
        return f"{self.marca_carro}, {self.ano}"
    
    def preco_formatado(self):
        return format_currency(self.preco, 'BRL', locale='pt_BR')



