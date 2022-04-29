from django.contrib import admin
from .models import Acessoria,Alterar, Produto ,Pedidos

admin.site.register(Acessoria)

admin.site.register(Alterar)

admin.site.register(Produto)

@admin.register(Pedidos)
class Pedidos(admin.ModelAdmin):
    search_fields = ('id',)
    list_display = ('pedido', 'produto','status')
    readonly_fields=('pedido','produto','status')
    list_filter = ('status',)