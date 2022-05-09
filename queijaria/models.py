from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cpf = models.IntegerField(default=00000000000)

    def get_group(self):
        return self.groups.name


class Fornecedor(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class RecebimentoLeite(models.Model):
    data = models.DateTimeField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    quantidade = models.FloatField(default=0)

class TipoProduto(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    tipo = models.ForeignKey(TipoProduto, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=40)

    class Meta:
        default_related_name = 'produto'

    def __str__(self) -> str:
        return self.nome

class Producao(models.Model):
    data = models.DateField(blank=False)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    leite = models.IntegerField(blank=False)
    sal = models.FloatField(default=0, blank=True)
    peso = models.FloatField(default=0, blank=True)
    rendimento = models.FloatField(default=0, blank=True)
    acucar = models.FloatField(default=0, blank=True)
    lote = models.IntegerField(blank=False)
    observacao = models.TextField(blank=True)

    class Meta:
        default_related_name = 'producao'

    def __str__(self) -> str:
        return str(self.lote)
