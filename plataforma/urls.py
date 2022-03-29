from django.urls import path
from . import views


urlpatterns = [
    path('',views.home ,name='home'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('valida/',views.valida,name='valida'),
    path('alterar/',views.alterar,name='alterar'),
    path('cancelar/',views.cancelar,name='cancelar'),
    path('declaracao/',views.declaracao,name='declaracao'),
    path('create-checkout-session/<int:id>', views.create_checkout_session, name="create_checkout_session"),
    path('Sucesso/',views.Sucesso,name='Sucesso'),
    path('Erro/',views.Erro,name='Erro'),
]