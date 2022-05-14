from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home.as_view(), name='home'),
    path('producao/recebimento-leite', views.recebimento_leite.as_view(), name='recebimento-leite'),
    path('producao/producao-diaria', views.produção_diaria.as_view(), name='producao-diaria'),
    path('producao/estoque', views.estoque.as_view(), name='estoque'),
    path('producao/clientes', views.clientes.as_view(), name='clientes'),
]