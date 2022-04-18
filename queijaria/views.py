from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

from queijaria.models import Fornecedor, RecebimentoLeite

class login(View):
    template_name = 'login.html'

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        if request.method != 'POST':
            return render(request, 'login.html')

        user = request.POST.get('usuario')
        password = request.POST.get('senha')

        if not user or not password:
            messages.error(request, "Preencha todos os campos")
            return render(request, 'login.html')

        userAuth = auth.authenticate(request, username=user, password=password)

        if not userAuth:
            messages.error(request, "Usuario ou senha Incorretos")
            return render(request, 'login.html')

        else:
            auth.login(request, userAuth)
            messages.success(request, "Usuario logado com sucesso")
            return redirect('home')

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        if request.method != 'POST':
            return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

class home(LoginRequiredMixin, View):
    login_url = 'queijaria/login/'

    def get(self, request):
        context = {
                'user' : request.user
            }
        return render(request, 'home.html', context)


class recebimento_leite(LoginRequiredMixin, View):
    login_url = 'queijaria/login/'


    def get(self, request):
        context = {
                'user' : request.user,
                'fornecedores': Fornecedor.objects.all(),
                'leites' : RecebimentoLeite.objects.all(),
                'leite_total' : RecebimentoLeite.objects.values('quantidade').aggregate(Sum('quantidade')),
            }
        return render(request, 'producao/recebimento_leite.html', context)

        
    def post(self, request):
        
        context = {
                'user' : request.user,
                'fornecedores': Fornecedor.objects.all(),
                'leites' : RecebimentoLeite.objects.all(),
                'leite_total' : RecebimentoLeite.objects.values('quantidade').aggregate(Sum('quantidade')),
            }


        dados = request.POST
        RecebimentoLeite.objects.create(data=dados.get('data'), fornecedor=Fornecedor.objects.get(nome=dados.get('fornecedor')), quantidade=dados.get('qnt'))
        return render(request, 'producao/recebimento_leite.html', context)