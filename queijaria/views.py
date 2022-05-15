from traceback import print_tb
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

from queijaria.models import Estoque, Fornecedor, Producao, Produto, RecebimentoLeite, Cliente, Venda

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
    login_url = 'login/'

    def get(self, request):
        context = {
                'user' : request.user
            }
        return render(request, 'home.html', context)

class recebimento_leite(LoginRequiredMixin, View):
    login_url = 'login/'


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

class produção_diaria(LoginRequiredMixin, View):
    login_url = 'login/'


    def get(self, request):
        table = Producao.objects.all()
        try:
            lote = Producao.objects.values_list('id').last()[0] + 1
        except:
            lote = 1

        context = {
                'user' : request.user,
                'produtos': Produto.objects.all(),
                'lote': lote,
                'producoes': table
            }

        return render(request, 'producao/producao_diaria.html', context)

        
    def post(self, request):
        try:
            lote = Producao.objects.values_list('id').last()[0] + 1
        except:
            lote = 1

        dados = request.POST

        dados = {
            'lote' : dados.get('lote'),
            'data' : dados.get('data'),
            'produto' : Produto.objects.filter(nome=dados.get('produto')).first(),
            'leite' : dados.get('leite'),
            'sal' : dados.get('sal'),
            'açucar' : dados.get('açucar'),
            'peso' : dados.get('peso'),
            'rendimento' : dados.get('rendimento'),
            'observação' : dados.get('observação'),
        }

        context = {
                'user' : request.user,
                'produtos': Produto.objects.all(),
                'lote': lote,
                'dados': dados
            }

        if dados['lote'] == '' or dados['data'] == '' or dados['produto'] == '' or dados['leite'] == '' or dados['peso'] == '':
            messages.error(request, "Os campos (lote, data, produto, leite, peso) não podem estar vazios. Preencha-os corretamente.")
            return render(request, 'producao/producao_diaria.html', context)

        if dados['sal'] == '' and dados['açucar'] == '':
            messages.error(request, "Um dos campos (sal, açucar) deve ser preenchido.")
            return render(request, 'producao/producao_diaria.html', context)

        if dados['sal'] != '' and dados['açucar'] != '':
            messages.error(request, "Apenas um dos campos (sal, açucar) deve ser preenchido.")
            return render(request, 'producao/producao_diaria.html', context)

        if dados['sal'] == '':
            dados['sal'] = 0

        if dados['açucar'] == '':
            dados['açucar'] = 0

        if dados['rendimento'] == '':
            dados['rendimento'] = 0
        
        if dados['observação'] == '':
            dados['observação'] = ''

        Producao.objects.create(
            lote = dados['lote'],
            data = dados['data'],
            produto = dados['produto'],
            leite = dados['leite'],
            sal = dados['sal'],
            peso = dados['peso'],
            acucar = dados['açucar'],
            rendimento = dados['rendimento'],
            observacao = dados['observação'],
        )

        try:
            estoque = Estoque.objects.filter(produto=dados['produto']).first()
            print(estoque.produto)
            qnt = estoque.quantidade
            peso = dados['peso']
            total = qnt+float(peso)
            estoque.quantidade = total
            estoque.save()
        except:
            if dados['produto'].tipo.nome == 'Queijo':
                uni = 'KG'
            else:
                uni = 'UNI'
            Estoque.objects.create(
                produto = dados['produto'],
                quantidade = dados['peso'],
                unidade = uni 
            )
        

        context['dados'] = {
            'leite' : '',
            'sal' : '',
            'açucar' : '',
            'peso' : '',
            'rendimento' : '',
            'observação' : '',
        }

        messages.success(request, "Produção inserida com sucesso.")
        return redirect('producao-diaria')

class clientes(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        cliente = Cliente.objects.all()
        cliente = list(map(lambda x: x.content_object, cliente))
        context = {
            'user' : request.user,
            'clientes' : cliente
            }
        return render(request, 'clientes/clientes.html', context)

class estoque(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        context = {
                'user' : request.user,
                'estoques': Estoque.objects.all(),

            }
        return render(request, 'estoque/estoque.html', context)

class vendas(LoginRequiredMixin, View):
    login_url= 'login/'

    def get(self, request):
        context = {
                'user' : request.user,
                'vendas': Venda.objects.all(),
            }
        print(context['vendas'])
        return render(request, 'vendas/vendas.html', context)