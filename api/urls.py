from django.contrib import admin
from django.urls import path, include
from .views import FornecedorViewSet, RecebimentoLeiteViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', UserViewSet, basename='Usuario')
router.register('fornecedores', FornecedorViewSet, basename='Fornecedor')
router.register('recebimento-leite', RecebimentoLeiteViewSet, basename='Recebimento-Leite')

urlpatterns = [
    path('', include(router.urls)),
]
