from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

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

class CategoriaProduto(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    tipo = models.ForeignKey(TipoProduto, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=40, unique=True)
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.DO_NOTHING, default=1)
    marca = models.CharField(max_length=25, default=0)
    codBarras = models.IntegerField(default=0)
    valorCompra = models.FloatField(default=0)
    valorVenda = models.FloatField(default=0)
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

class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.DO_NOTHING)
    quantidade = models.FloatField(default=0)
    unidade = models.CharField(max_length=20)

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class PessoaFisica(Pessoa):
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    nascimento = models.DateField(blank=True)


class PessoaJuridica(Pessoa):
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    inscricao_estadual = models.CharField(max_length=20)


class Cliente(models.Model):
    limite = models.Q(model = 'pessoafisica') | models.Q(model = 'pessoajuridica')
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, limit_choices_to=limite) 
    object_id = models.PositiveIntegerField() 
    content_object=GenericForeignKey('content_type', 'object_id')

class ItemVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING, blank=False)
    quantidade = models.FloatField(blank=False)


class Venda(models.Model):
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    items = models.ManyToManyField(ItemVenda)
    total = models.FloatField()
    faturamento = models.CharField(max_length=25)
    vencimento = models.DateField()


