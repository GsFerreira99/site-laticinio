from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login.as_view(), name='login'),
    path('', views.home.as_view(), name='home'),
    path('producao/recebimento-leite', views.recebimento_leite.as_view(), name='recebimento-leite'),
]