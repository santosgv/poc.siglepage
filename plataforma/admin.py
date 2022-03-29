from django.contrib import admin
from .models import Acessoria, Produto ,Pedidos

admin.site.register(Acessoria)

admin.site.register(Produto)

@admin.register(Pedidos)
class Pedidos(admin.ModelAdmin):
    list_display = ('pedido', 'produto')
    readonly_fields=('pedido','produto',)
