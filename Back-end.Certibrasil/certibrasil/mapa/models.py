from django.utils import timezone  
from django.db import models  
from django.urls import reverse
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)  # Alterado para CharField
    cnpj = models.CharField(max_length=14, unique=True)

    def _str_(self):
        return self.nome

class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='enderecos', on_delete=models.CASCADE)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)  # Alterado para CharField
    cep = models.CharField(max_length=10, null=True, blank=True)  # Alterado para CharField
    pais = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.rua}, {self.cidade}"

class Certificacao(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='certificacoes', on_delete=models.CASCADE)
    nome_do_produto = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_do_pedido = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Certificação {self.id} - {self.cliente.nome}"