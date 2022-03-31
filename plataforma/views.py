import json
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail
from .models import Acessoria,Produto,Pedidos
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

stripe.api_key= settings.STRIPE_SECRET_KEY

def home(request):
    return render(request,'home.html')

def cadastro(request):
    return render(request,'cadastro.html')

@csrf_exempt
def create_payment(request,id):
    pedido =Pedidos.objects.get(id=id) 

    # Create a PaymentIntent with the order amount and currency
    intent = stripe.PaymentIntent.create(
    amount= int(pedido.id),
    currency='BRL',
            
        )
    return JsonResponse({
        'clientSecret': intent['client_secret']
        })
  

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)


    print(event)
    if event['type'] == 'charge.succeeded':
        session = event['data']['object']
        pedido =Pedidos.objects.get(id=id)
        #mensagem =f'''
        #Segue dados do Cadastro
        #com sucesso
        #'''
        
        #send_mail('Pagamento realizado',mensagem,'santosgomesv@gmail.com',recipient_list=['vitormystore@gmail.com'])
        return HttpResponse(status=200)

def valida(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    cpf = request.POST.get('cpf')
    rg = request.POST.get('rg')
    ExpeditorRG = request.POST.get('ExpeditorRG')
    uf_rg = request.POST.get('uf_rg')
    Data_Nascimento = request.POST.get('Data_Nascimento')
    Nome_Mae = request.POST.get('Nome_Mae')
    Banco = request.POST.get('Banco')
    Imposto = request.POST.get('Imposto')
    Nome_Fantasia = request.POST.get('Nome_Fantasia')
    Capitao_Inicial =request.POST.get('Capitao_Inicial')
    OcupacaoPrincipal = request.POST.get('OcupacaoPrincipal')
    OcupacaoSegundario = request.POST.get('OcupacaoSegundario')
    cep = request.POST.get('cep')
    Rua = request.POST.get('Rua')
    Numero = request.POST.get('Numero')
    Complemento = request.POST.get('Complemento')
    Bairro = request.POST.get('Bairro')
    Cidade = request.POST.get('Cidade')
    Estado = request.POST.get('Estado')

    Cadastro =Acessoria(nome = nome, 
                        email= email,
                        CPF =cpf,
                        telefone=telefone,
                        RG = rg,
                        ExpeditorRG =ExpeditorRG,
                        UF_RG =uf_rg,
                        Data_Nascimento = Data_Nascimento,
                        Nome_Mae = Nome_Mae,
                        Banco = Banco,
                        Imposto = Imposto,
                        Nome_Fantasia =Nome_Fantasia ,
                        Capitao_Inicial = Capitao_Inicial,
                        OcupacaoPrincipal = OcupacaoPrincipal,
                        OcupacaoSegundario = OcupacaoSegundario,
                        CEP =cep ,
                        Rua = Rua,
                        Numero =Numero,
                        Complemento =Complemento,
                        Bairro =Bairro,
                        Cidade =Cidade ,
                        Estado =Estado,
                        
                        )
    Cadastro.save()

    produto =Produto.objects.get(id=1)
   
    pedido =Pedidos(pedido=Cadastro, produto=produto ,valor=produto.preco)
    pedido.save()
  

    mensagem =f'''
    Segue dados do Cadastro
    {Cadastro.nome}
    {Cadastro.email}
    {Cadastro.Nome_Fantasia}
    '''
    #send_mail('Pagamento realizado',mensagem,'santosgomesv@gmail.com',recipient_list=[email])
    return render(request,'pagamento.html',{'pedido':pedido, 'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUPLIC_KEY})
    #return HttpResponse(Cadastro.email)


def alterar(request):
    return render(request,'altera.html')

def cancelar(request):
    return render(request,'cancela.html')

def declaracao(request):
    return render(request,'declaracao.html')

def Sucesso(request):
    return render(request,'Sucesso.html')

def Erro(request):
    return render(request,'Erro.html')