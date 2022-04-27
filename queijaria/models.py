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


