from django.urls import path
from . import views


urlpatterns = [
    path('',views.home ,name='home'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('valida/',views.valida,name='valida'),
    path('alterar/',views.alterar,name='alterar'),
    path('cancelar/',views.cancelar,name='cancelar'),
    path('declaracao/',views.declaracao,name='declaracao'),
    path('create-payment-intent/<int:id>', views.create_payment, name="create_payment-intent"),
    path('Sucesso/',views.Sucesso,name='Sucesso'),
    path('Erro/',views.Erro,name='Erro'),
    path('stripe_webhook', views.stripe_webhook, name="stripe_webhook")
]