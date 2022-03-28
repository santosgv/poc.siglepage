
from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail
from .models import Acessoria

def home(request):
    return render(request,'home.html')

def cadastro(request):
    return render(request,'cadastro.html',{})

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
                        Estado =Estado
                        )
    #Cadastro.save()
    mensagem =f'''
    Segue dados do Cadastro
    {Cadastro.nome}
    {Cadastro.email}
    {Cadastro.Nome_Fantasia}
    '''
    send_mail('Pagamento realizado',mensagem,'santosgomesv@gmail.com',recipient_list=[email])
    #return render(request,'pagamento.html')
    return HttpResponse(Cadastro.email)


def alterar(request):
    return render(request,'altera.html')

def cancelar(request):
    return render(request,'cancela.html')

def declaracao(request):
    return render(request,'declaracao.html')