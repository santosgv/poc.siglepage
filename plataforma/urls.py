from django.urls import path
from . import views


urlpatterns = [
    path('',views.home ,name='home'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('valida/',views.valida,name='valida'),
    path('alterar/',views.alterar,name='alterar'),
    path('cancelar/',views.cancelar,name='cancelar'),
    path('declaracao/',views.declaracao,name='declaracao'),
]