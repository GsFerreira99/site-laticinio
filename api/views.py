from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from api.serializers import FornecedorSerializer, ProducaoSerializer, ProdutoSerializer, RecebimentoLeiteSerializer, UserSerializer
from queijaria.models import Fornecedor, Producao, Produto, RecebimentoLeite, User

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
        fornecedor = Fornecedor.objects.filter(nome=request.data['fornecedor'])
        request.data['fornecedor'] = fornecedor[0].id

        entrada_serializer = self.get_serializer(data=request.data)
        entrada_serializer.is_valid(raise_exception=True)
        self.perform_create(entrada_serializer)
        headers = self.get_success_headers(entrada_serializer.data)
        return Response(entrada_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ProducaoViewSet(viewsets.ModelViewSet):
    """Listagem da Produção"""

    serializer_class = ProducaoSerializer
    queryset = Producao.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):

        request.data['produto'] = Produto.objects.filter(nome=request.data['produto'])[0].id
        print(request.data)

        if request.data['sal'] == '': request.data['sal'] = 0
        if request.data['acucar'] == '': request.data['acucar'] = 0
        if request.data['peso'] == '': request.data['peso'] = 0
        if request.data['rendimento'] == '': request.data['rendimento'] = 0

        entrada_serializer = self.get_serializer(data=request.data)
        entrada_serializer.is_valid(raise_exception=True)
        self.perform_create(entrada_serializer)
        headers = self.get_success_headers(entrada_serializer.data)
        
        return Response(entrada_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProdutoViewSet(viewsets.ReadOnlyModelViewSet):
    """Listagem da Produção"""

    serializer_class = ProdutoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Produto.objects.all()
