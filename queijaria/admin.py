from django.contrib import admin
from .models import Cliente, Estoque, Fornecedor, ItemVenda, PessoaFisica, PessoaJuridica, RecebimentoLeite, User, Producao, Produto, TipoProduto, CategoriaProduto, Venda
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('cpf',)}),
    )

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)

class TipoProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'nome',)

class ProducaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'lote', 'produto', 'peso', 'rendimento',)

class RecebimentoLeiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'fornecedor', 'quantidade',)

class CategoriaProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'unidade', 'quantidade')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_object')

class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf')

class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj')

class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'quantidade')

class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'cliente', 'total', 'vencimento')

admin.site.register(User, MyUserAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(TipoProduto, TipoProdutoAdmin)
admin.site.register(Producao, ProducaoAdmin)
admin.site.register(RecebimentoLeite, RecebimentoLeiteAdmin)
admin.site.register(CategoriaProduto, CategoriaProdutoAdmin)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(PessoaFisica, PessoaFisicaAdmin)
admin.site.register(PessoaJuridica, PessoaJuridicaAdmin)
admin.site.register(ItemVenda, ItemVendaAdmin)
admin.site.register(Venda, VendaAdmin)