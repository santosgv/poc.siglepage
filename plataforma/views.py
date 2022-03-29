
from django.http import JsonResponse
from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail
from .models import Acessoria,Produto,Pedidos
import stripe
from django.conf import settings

stripe.api_key= settings.STRIPE_SECRET_KEY

def home(request):
    produto =Produto.objects.get(id=1)
    return render(request,'home.html',{'produto':produto,'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUPLIC_KEY})

def cadastro(request):
    return render(request,'cadastro.html',{})


def create_checkout_session(request, id):
    produto = Produto.objects.get(id = id)
    YOUR_DOMAIN = "http://127.0.0.1:8000"
    checkout_session = stripe.checkout.Session.create(
    line_items=[
            {
            'price_data': {
            'currency': 'BRL',
            'unit_amount': int(produto.preco),
            'product_data': {
            'name': produto.nome
                            }
                            },
            'quantity': 1,
            },
                ],
    payment_method_types=[
            'card',
            'boleto',
                ],
    metadata={
            'id_produto': produto.id,
            },
    mode='payment',
    success_url=YOUR_DOMAIN + '/sucesso',
    cancel_url=YOUR_DOMAIN + '/erro',
        )
    return JsonResponse({'id': checkout_session.id})

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
    
    pedido =Pedidos(pedido=Cadastro, produto=produto)
    pedido.save()

    mensagem =f'''
    Segue dados do Cadastro
    {Cadastro.nome}
    {Cadastro.email}
    {Cadastro.Nome_Fantasia}
    '''
    #send_mail('Pagamento realizado',mensagem,'santosgomesv@gmail.com',recipient_list=[email])
    return render(request,'pagamento.html')
    #return HttpResponse(Cadastro.email)


def alterar(request):
    return render(request,'altera.html')

def cancelar(request):
    return render(request,'cancela.html')

def declaracao(request):
    return render(request,'declaracao.html')

def sucesso(request):
    return HttpResponse('Sucesso')

def erro(request):
    return HttpResponse('Erro')