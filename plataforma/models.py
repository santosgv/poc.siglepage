from pyexpat import model
from django.db import models


class Acessoria(models.Model):
    nome = models.CharField(max_length=200)
    CPF = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    email2 = models.CharField(blank=True ,null=True,max_length=50)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    logingov = models.CharField(max_length=10)
    senhagov = models.CharField(max_length=10)
    Data_Nascimento = models.CharField(max_length=10)
    nome_Impresarial = models.CharField(max_length=100)
    nacionalidade =models.CharField(max_length=20)
    sexo = models.CharField(max_length=10)
    Nome_Mae = models.CharField(max_length=200)
    tituloeleitor= models.CharField(max_length=100)
    RG = models.CharField(max_length=15)
    ExpeditorRG = models.CharField(max_length=10)
    UF_RG = models.CharField(max_length=2)
    Nome_Fantasia = models.CharField(max_length=250)
    Capitao_Inicial = models.CharField(max_length=15)
    OcupacaoPrincipal = models.CharField(max_length=500)
    OcupacaoSegundario = models.TextField(max_length=500)
    formaatuacao = models.TextField(blank=True ,null=True,max_length=100)  
    CEP = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    Numero = models.CharField(max_length=5)
    Complemento = models.CharField(max_length=50)
    Bairro = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Estado = models.CharField(max_length=2)
    residencial_CEP = models.CharField(blank=True, null=True,max_length=15)
    residencial_logradouro = models.CharField(blank=True,null=True,max_length=200)
    residencial_Numero = models.CharField(blank=True ,null=True,max_length=5)
    residencial_Complemento = models.CharField(blank=True,null=True,max_length=50)
    residencial_Bairro = models.CharField(blank=True,null=True,max_length=50)
    residencial_Cidade = models.CharField(blank=True,null=True,max_length=50)
    residencial_Estado = models.CharField(blank=True,null=True,max_length=2)
    

    def __str__(self):
        return self.CPF

class Alterar(models.Model):
    cnpj = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    datanascimento = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    nomeEmpresarial = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=200)
    sexo = models.CharField(max_length=15)
    nome_mae = models.CharField(max_length=200)
    rg = models.CharField(max_length=200)
    ExpeditorRG = models.CharField(max_length=200)
    uf_rg = models.CharField(max_length=200)
    Nome_Fantasia = models.CharField(max_length=200)
    Capitao_Inicial = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    Celular = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    OcupacaoPrimaria = models.CharField(max_length=200)
    Ocupacao_Segundaria = models.CharField(max_length=200)
    formaatuacao =models.CharField(max_length=200)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    estadocnpj = models.CharField(max_length=2)
    contagov = models.CharField(max_length=50)
    senhagov = models.CharField(max_length=50)
    cep2 = models.CharField(blank=True,null=True,max_length=8)
    lagradouro2 = models.CharField(blank=True,null=True,max_length=100)
    numero2 = models.CharField(blank=True,null=True,max_length=5)
    complemento2 = models.CharField(blank=True,null=True,max_length=20)
    bairro2 = models.CharField(blank=True,null=True,max_length=100)
    municipio2 = models.CharField(blank=True,null=True,max_length=100)
    estadocnpj2 = models.CharField(blank=True,null=True,max_length=2)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField(max_length=5)


    def __str__(self) -> str:
        return self.nome

class Pedidos(models.Model):
    pedido = models.ForeignKey(Acessoria, on_delete= models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete= models.CASCADE)
    status =models.CharField(max_length=100)

    def __str__(self) -> int:
        return str(self.id)