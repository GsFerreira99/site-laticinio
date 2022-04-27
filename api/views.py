import re
from unicodedata import name
from urllib import response
from venv import create
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import Group
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.serializers import FornecedorSerializer, RecebimentoLeiteSerializer, UserSerializer
from queijaria.models import Fornecedor, RecebimentoLeite, User

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Retorna os dados do usuario autenticado"""
    
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(username=user)
        return queryset

class FornecedorViewSet(viewsets.ReadOnlyModelViewSet):
    """Exibindo todos os fornecedores"""

    serializer_class = FornecedorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        fornecedores = Fornecedor.objects.all()
        return fornecedores

class RecebimentoLeiteViewSet(viewsets.ModelViewSet):
    """Listagem dos recebimentos de leite"""

    serializer_class = RecebimentoLeiteSerializer
    queryset = RecebimentoLeite.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        print(request.data)
        fornecedor = Fornecedor.objects.filter(nome=request.data['fornecedor'])
        print(fornecedor)
        request.data['fornecedor'] = fornecedor[0].id
        print(request.data)

        entrada_serializer = self.get_serializer(data=request.data)
        entrada_serializer.is_valid(raise_exception=True)
        self.perform_create(entrada_serializer)
        headers = self.get_success_headers(entrada_serializer.data)
        return Response(entrada_serializer.data, status=status.HTTP_201_CREATED, headers=headers)