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
    produto =Produto.objects.get(id=id)

    id_prod =json.loads(request.body)['produto']
    id_cadastro=json.loads(request.body)['id_cadastro']
    nome = json.loads(request.body)['nome']
    email = json.loads(request.body)['email']
    telefone = json.loads(request.body)['telefone']
    cpf = json.loads(request.body)['cpf']
    rg = json.loads(request.body)['rg']
    ExpeditorRG = json.loads(request.body)['ExpeditorRG']
    uf_rg = json.loads(request.body)['uf_rg']
    Data_Nascimento = json.loads(request.body)['Data_Nascimento']
    Nome_Mae = json.loads(request.body)['Nome_Mae']
    Banco = json.loads(request.body)['Banco']
    Imposto = json.loads(request.body)['Imposto']
    Nome_Fantasia = json.loads(request.body)['Nome_Fantasia']
    Capitao_Inicial = json.loads(request.body)['Capitao_Inicial']
    OcupacaoPrincipal = json.loads(request.body)['OcupacaoPrincipal']
    OcupacaoSegundario = json.loads(request.body)['OcupacaoSegundario']
    cep = json.loads(request.body)['cep']
    Rua = json.loads(request.body)['Rua']
    Numero = json.loads(request.body)['Numero']
    Complemento = json.loads(request.body)['Complemento']
    Bairro = json.loads(request.body)['Bairro']
    Cidade = json.loads(request.body)['Cidade']
    Estado = json.loads(request.body)['Estado']


    # Create a PaymentIntent with the order amount and currency
    intent = stripe.PaymentIntent.create(
    amount= int(produto.preco *100),
    currency='BRL',
    metadata={
        'id_prod':id_prod,
        'id_cadastro':id_cadastro,
        'nome':nome,
        'email':email,
        'telefone':telefone,
        'cpf':cpf,
        'rg':rg,
        'ExpeditorRG':ExpeditorRG,
        'uf_rg':uf_rg,
        'Data_Nascimento':Data_Nascimento,
        'Nome_Mae':Nome_Mae,
        'Banco':Banco,
        'Imposto':Imposto,
        'Nome_Fantasia':Nome_Fantasia,
        'Capitao_Inicial':Capitao_Inicial,
        'OcupacaoPrincipal':OcupacaoPrincipal,
        'OcupacaoSegundario':OcupacaoSegundario,
        'cep':cep,
        'Rua':Rua,
        'Numero':Numero,
        'Complemento':Complemento,
        'Bairro':Bairro,
        'Cidade':Cidade,
        'Estado':Estado,
    }   
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

    
  
    if event['type'] == 'charge.succeeded':
        session = event['data']['object']
    
        #pedido = Pedidos(Acessoria.objects.filter(pedido=session['metadata']['id_cadastro']), produto =Produto.objects.get(id=session['metadata']['id_prod']) ,status=event['type'])
        #pedido.save
        
        print(session)
        mensagem =f'''
        Segue dados do Cadastro no MEI CERTO
        {session['metadata']['id_prod']}
        {session['metadata']['id_cadastro']}
        {session['metadata']['id_prod']}
        {session['metadata']['nome']}
        {session['metadata']['email']}
        {session['metadata']['telefone']}
        {session['metadata']['cpf']}
        {session['metadata']['rg']}
        {session['metadata']['ExpeditorRG']}
        {session['metadata']['uf_rg']}
        {session['metadata']['Data_Nascimento']}
        {session['metadata']['Nome_Mae']}
        {session['metadata']['Banco']}
        {session['metadata']['Imposto']}
        {session['metadata']['Nome_Fantasia']}
        {session['metadata']['Capitao_Inicial']}
        {session['metadata']['OcupacaoPrincipal']}
        {session['metadata']['OcupacaoSegundario']}
        {session['metadata']['cep']}
        {session['metadata']['Rua']}
        {session['metadata']['Numero']}
        {session['metadata']['Complemento']}
        {session['metadata']['Bairro']}
        {session['metadata']['Cidade']}
        {session['metadata']['Estado']}
        '''

        return send_mail('Pagamento realizado com sucesso',mensagem,'santosgomesv@gmail.com',recipient_list=[session['metadata']['email'],'precoflix@gmail.com'])

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
   
    return render(request,'pagamento.html',{'cadastro':Cadastro,'produto':produto, 'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUPLIC_KEY})



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