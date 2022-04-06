from django.urls import path
from . import views


urlpatterns = [
    path('',views.home ,name='home'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('valida/',views.valida,name='valida'),
    path('alterar/',views.alterar,name='alterar'),
    path('cancelar/',views.cancelar,name='cancelar'),
    path('declaracao/',views.declaracao,name='declaracao'),
    path('dividaativa/',views.dividaativa,name='dividaativa'),
    path('educacao/',views.educacao,name='educacao'),
    path('faleconosco/',views.faleconosco,name='faleconosco'),
    path('create-payment-intent/<int:id>', views.create_payment, name="create_payment-intent"),
    path('stripe_webhook', views.stripe_webhook, name="stripe_webhook")
]