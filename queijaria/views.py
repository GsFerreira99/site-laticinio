from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.views import View

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

class home(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'nome' : f'{request.user.first_name} {request.user.last_name}',
                'funcao' : request.user.groups.first()
            }
            return render(request, 'home.html', context)
        else:
            return redirect('login')

class recebimento_leite(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'user' : request.user
            }
            return render(request, 'producao/recebimento_leite.html', context)
        else:
            return redirect('login')
        