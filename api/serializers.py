from dataclasses import fields
from re import T
from rest_framework import serializers
from queijaria.models import Producao, Produto, RecebimentoLeite, User, Fornecedor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'groups']

class FornecedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fornecedor
        fields = ['id', 'nome']

class RecebimentoLeiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecebimentoLeite
        fields = ['id', 'data', 'fornecedor', 'quantidade']

class ProducaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producao
        fields = ['id', 'data', 'produto', 'leite', 'sal', 'peso', 'rendimento', 'acucar', 'lote', 'observacao']

class ProdutoSerializer(serializers.ModelSerializer):
    tipo = serializers.StringRelatedField()
    class Meta:
        model = Produto
        fields = ['id', 'tipo', 'nome']