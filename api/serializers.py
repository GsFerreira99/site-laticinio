from dataclasses import fields
from rest_framework import serializers
from queijaria.models import RecebimentoLeite, User, Fornecedor

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