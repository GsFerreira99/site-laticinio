from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class login(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, 'login.html')

class home(View):

    def get(self, request):
        return render(request, 'home.html')

class recebimento_leite(View):

    def get(self, request):
        return render(request, 'producao/recebimento_leite.html')