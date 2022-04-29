from cgitb import reset
import json
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail
from .models import Acessoria,Alterar,Produto,Pedidos
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
    receipt_email=email,
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
        
        
        cadastro =Acessoria.objects.get(id=session['metadata']['id_cadastro'])
        prod =Produto.objects.get(id=1)
    
        pedido = Pedidos(pedido=cadastro, produto =prod,status='Pagamento aprovado')
        pedido.save()
        
        
        mensagem =f'''
        Segue numero do pedido do Cadastro no MEI CERTO
        {pedido.id}
        '''
        return send_mail('Pagamento realizado com sucesso',mensagem,'santosgomesv@gmail.com',recipient_list=[session['metadata']['email'],'precoflix@gmail.com'])

def valida(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    email2 = request.POST.get('email2')
    telefone = request.POST.get('telefone')
    celular = request.POST.get('Celular')
    logingov = request.POST.get('contagome')
    senhagov = request.POST.get('senhacontagome')
    Data_Nascimento = request.POST.get('Data_Nascimento')
    nomeimpressarial = request.POST.get('nomeempresarial')
    nacionalidade = request.POST.get('nacionalidade')
    sexo = request.POST.get('SEXO')
    nomemae= request.POST.get('nomemae')
    tituloeleitor = request.POST.get('tituloeleitor')
    rg = request.POST.get('rg')
    ExpeditorRG = request.POST.get('ExpeditorRG')
    uf_rg = request.POST.get('uf_rg')
    Nome_Fantasia = request.POST.get('Nome_Fantasia')
    Capitao_Inicial =request.POST.get('Capitao_Inicial')
    OcupacaoPrimaria = request.POST.get('OcupacaoPrimaria')
    OcupacaoSegundario = request.POST.getlist('Ocupacao_Segundaria')
    formaatuacao = request.POST.getlist('checks')
    cep = request.POST.get('cep')
    Rua = request.POST.get('logradouro')
    Numero = request.POST.get('numero')
    Complemento = request.POST.get('complemento')
    Bairro = request.POST.get('bairro')
    Cidade = request.POST.get('Cidade')
    Estado = request.POST.get('uf1')
    residencial_cep = request.POST.get('cep2')
    residencial_logradouro = request.POST.get('logradouro2')
    residencial_Numero = request.POST.get('numero2')
    residencial_Complemento = request.POST.get('complemento2')
    residencial_Bairro = request.POST.get('bairro2')
    residencial_Cidade = request.POST.get('municipio2')
    residencial_Estado = request.POST.get('estadocnpj2')

    Cadastro =Acessoria(
        nome = nome,
        CPF =cpf,
        email = email,
        email2 = email2,
        telefone = telefone,
        celular = celular,
        logingov = logingov,
        senhagov = senhagov,
        Data_Nascimento = Data_Nascimento,
        nome_Impresarial = nomeimpressarial,
        nacionalidade = nacionalidade,
        sexo = sexo,
        Nome_Mae= nomemae,
        tituloeleitor = tituloeleitor,
        RG = rg,
        ExpeditorRG = ExpeditorRG,
        UF_RG = uf_rg,
        Nome_Fantasia = Nome_Fantasia,
        Capitao_Inicial = Capitao_Inicial,
        OcupacaoPrincipal = OcupacaoPrimaria,
        OcupacaoSegundario = OcupacaoSegundario,
        formaatuacao = formaatuacao,
        CEP = cep,
        logradouro = Rua,
        Numero = Numero,
        Complemento = Complemento,
        Bairro = Bairro,
        Cidade = Cidade,
        Estado = Estado,
        residencial_CEP = residencial_cep,
        residencial_logradouro = residencial_logradouro,
        residencial_Numero = residencial_Numero,
        residencial_Complemento = residencial_Complemento,
        residencial_Bairro = residencial_Bairro,
        residencial_Cidade = residencial_Cidade,
        residencial_Estado = residencial_Estado,
    )
    Cadastro.save()
  
    produto =Produto.objects.get(id=1)

    return render(request,'pagamento.html',{'cadastro':Cadastro,'produto':produto, 'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUPLIC_KEY})

def alterar(request):
    return render(request,'altera.html')

def validaalterar(request):
    cnpj = request.POST.get('cnpj')
    cpf = request.POST.get('cpf')
    datanascimento = request.POST.get('Data_Nascimento')
    nome = request.POST.get('nome')
    nomeEmpresarial = request.POST.get('nomeEmpresarial')
    nacionalidade = request.POST.get('nacionalidade')
    sexo = request.POST.get('sexo')
    nome_mae = request.POST.get('nome_mae')
    rg = request.POST.get('rg')
    ExpeditorRG = request.POST.get('ExpeditorRG')
    uf_rg = request.POST.get('uf_rg')
    Nome_Fantasia = request.POST.get('Nome_Fantasia')
    Capitao_Inicial = request.POST.get('Capitao_Inicial')
    telefone = request.POST.get('telefone')
    Celular = request.POST.get('Celular')
    email = request.POST.get('email')
    OcupacaoPrimaria = request.POST.get('OcupacaoPrimaria')
    Ocupacao_Segundaria = request.POST.get('Ocupacao_Segundaria')
    formaatuacao = request.POST.getlist('checks')
    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    numero = request.POST.get('numero')
    complemento = request.POST.get('complemento')
    bairro = request.POST.get('bairro')
    municipio = request.POST.get('municipio')
    estadocnpj = request.POST.get('estadocnpj')
    contagov = request.POST.get('contagov')
    senhagov = request.POST.get('senhagov')
    cep2 = request.POST.get('cep2')
    lagradouro2 = request.POST.get('lagradouro2')
    numero2 = request.POST.get('numero2')
    complemento2 = request.POST.get('complemento2')
    bairro2 = request.POST.get('bairro2')
    municipio2 = request.POST.get('municipio2')
    estadocnpj2 = request.POST.get('estadocnpj2')

    AlterarMei =Alterar(
    cnpj = cnpj,
    cpf = cpf,
    datanascimento = datanascimento,
    nome = nome,
    nomeEmpresarial = nomeEmpresarial,
    nacionalidade = nacionalidade,
    sexo = sexo,
    nome_mae = nome_mae,
    rg = rg,
    ExpeditorRG = ExpeditorRG,
    uf_rg = uf_rg,
    Nome_Fantasia = Nome_Fantasia,
    Capitao_Inicial = Capitao_Inicial,
    telefone = telefone,
    Celular = Celular,
    email = email,
    OcupacaoPrimaria = OcupacaoPrimaria,
    Ocupacao_Segundaria = Ocupacao_Segundaria,
    formaatuacao = formaatuacao,
    cep = cep,
    rua = rua,
    numero = numero,
    complemento = complemento,
    bairro = bairro,
    municipio = municipio,
    estadocnpj = estadocnpj,
    contagov = contagov,
    senhagov = senhagov,
    cep2 = cep2,
    lagradouro2 = lagradouro2,
    numero2 = numero2,
    complemento2 = complemento2,
    bairro2 = bairro2,
    municipio2 = municipio2,
    estadocnpj2 = estadocnpj2
    )

    AlterarMei.save()

    produto =Produto.objects.get(id=2)
    return HttpResponse(request,'pagamento.html',{'altera':Alterar,'produto':produto, 'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUPLIC_KEY})


def cancelar(request):
    return render(request,'cancela.html')

def validacancelar(request):
    
    return HttpResponse('Cancelado')

def declaracao(request):
    return render(request,'declaracao.html')

def dividaativa(request):
    return render(request,'dividaativa.html')

def educacao(request):
    return render(request,'educacao.html')

def faleconosco(request):
    return render(request,'faleconosco.html')