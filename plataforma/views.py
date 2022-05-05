
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

        prod =Produto.objects.get(id=id)
    
        pedido = Pedidos(pedido=cadastro, produto = prod ,status='Pagamento aprovado')
        pedido.save()
        
        
        mensagem =f'''
        Segue numero do pedido no MEI CERTO
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
    senhagov = request.POST.get('senhacontagov')
    cep2 = request.POST.get('cep2')
    logradouro2 = request.POST.get('lagradouro2')
    numero2 = request.POST.get('numero2')
    complemento2 = request.POST.get('complemento2')
    bairro2 = request.POST.get('bairro2')
    municipio2 = request.POST.get('municipio2')
    estadocnpj2 = request.POST.get('estadocnpj2')

    AlterarMei = Acessoria(
    cnpj = cnpj,
    CPF = cpf,
    Data_Nascimento = datanascimento,
    nome = nome,
    nome_Impresarial = nomeEmpresarial,
    nacionalidade = nacionalidade,
    sexo = sexo,
    Nome_Mae = nome_mae,
    RG = rg,
    ExpeditorRG = ExpeditorRG,
    UF_RG = uf_rg,
    Nome_Fantasia = Nome_Fantasia,
    Capitao_Inicial = Capitao_Inicial,
    telefone = telefone,
    celular = Celular,
    email = email,
    OcupacaoPrincipal = OcupacaoPrimaria,
    OcupacaoSegundario = Ocupacao_Segundaria,
    formaatuacao = formaatuacao,
    CEP = cep,
    logradouro = rua,
    Numero = numero,
    Complemento = complemento,
    Bairro = bairro,
    Cidade = municipio,
    Estado = estadocnpj,
    logingov = contagov,
    senhagov = senhagov,
    residencial_CEP = cep2,
    residencial_logradouro = logradouro2,
    residencial_Numero = numero2,
    residencial_Complemento = complemento2,
    residencial_Bairro = bairro2,
    residencial_Cidade = municipio2,
    residencial_Estado = estadocnpj2,
    )

    AlterarMei.save()

    produto =Produto.objects.get(id=2)

    return render(request,'pagamento.html',{'cadastro':AlterarMei, 'produto':produto, 'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUPLIC_KEY})


def cancelar(request):
    return render(request,'cancela.html')

def validacancelar(request):
    cnpj = request.POST.get('cnpj')
    Nome_Fantasia = request.POST.get('nome_fantasia')
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    Data_Nascimento = request.POST.get('Data_Nascimento')
    Nome_Mae = request.POST.get('nome_mae')
    telefone = request.POST.get('telefone')
    email = request.POST.get('email')
    logingov = request.POST.get('contagov')
    senhagov = request.POST.get('senhacontagov')
    cep = request.POST.get('cep')
    Rua = request.POST.get('rua')
    Numero = request.POST.get('numero')
    Complemento = request.POST.get('complemento')
    Bairro = request.POST.get('bairro')
    Cidade = request.POST.get('municipio')
    Estado = request.POST.get('estadocnpj')
    
    BaixarMei =Acessoria(
        cnpj = cnpj,
        Nome_Fantasia = Nome_Fantasia,
        nome = nome,
        CPF = cpf,
        Data_Nascimento = Data_Nascimento,
        Nome_Mae =Nome_Mae ,
        telefone= telefone,
        email = email,
        logingov  = logingov,
        senhagov = senhagov,
        CEP = cep,
        logradouro = Rua,
        Numero = Numero,
        Complemento = Complemento,
        Bairro = Bairro,
        Cidade = Cidade,
        Estado = Estado,
    )
    BaixarMei.save()

    produto =Produto.objects.get(id=3)

    return render(request,'pagamento.html',{'cadastro':BaixarMei, 'produto':produto, 'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUPLIC_KEY})
    

def declaracao(request):
    return render(request,'declaracao.html')

def validadeclaracao(request):
    cnpj = request.POST.get('cnpj')
    Nome_Fantasia = request.POST.get('nome_fantasia')
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    revenda = request.POST.get('revenda_mercadoria')
    prestacao = request.POST.get('prestacao')
    transporte = request.POST.get('trasporte_de_carga')
    telefone = request.POST.get('telefone')
    email = request.POST.get('email')
    logingov = request.POST.get('contagov')
    senhagov = request.POST.get('senhacontagov')
    contratacao = request.POST.getlist('contratacao')
    funcionario = request.POST.getlist('func')
    
    Declaracao =Acessoria(
        cnpj = cnpj,
        Nome_Fantasia = Nome_Fantasia,
        nome = nome,
        CPF = cpf,
        revenda_mercadoria = revenda,
        prestacao = prestacao,
        trasporte_de_carga = transporte,
        telefone= telefone,
        email = email,
        logingov  = logingov,
        senhagov = senhagov,
        contratacao =contratacao,
        funcionario = funcionario,
    )
    Declaracao.save()

    produto =Produto.objects.get(id=4)
    return render(request,'pagamento.html',{'cadastro':Declaracao, 'produto':produto, 'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUPLIC_KEY})

def dividaativa(request):
    return render(request,'dividaativa.html')

def educacao(request):
    return render(request,'educacao.html')

def faleconosco(request):
    return render(request,'faleconosco.html')