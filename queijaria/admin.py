from django.contrib import admin
from .models import Fornecedor, RecebimentoLeite, User, Producao, Produto, TipoProduto
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

admin.site.register(User, MyUserAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(TipoProduto, TipoProdutoAdmin)
admin.site.register(Producao, ProducaoAdmin)
admin.site.register(RecebimentoLeite, RecebimentoLeiteAdmin)