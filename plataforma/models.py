from pyexpat import model
from django.db import models


class Acessoria(models.Model):
    cnpj = models.CharField(blank=True ,null=True,max_length=18)
    nome = models.CharField(max_length=200)
    CPF = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    email2 = models.CharField(blank=True ,null=True,max_length=50)
    telefone = models.CharField(blank=True ,null=True ,max_length=15)
    celular = models.CharField(blank=True ,null=True ,max_length=15)
    logingov = models.CharField(max_length=100)
    senhagov = models.CharField(max_length=100)
    Data_Nascimento = models.CharField(max_length=10)
    nome_Impresarial = models.CharField(blank=True ,null=True , max_length=100)
    nacionalidade =models.CharField(blank=True ,null=True , max_length=20)
    sexo = models.CharField(blank=True ,null=True , max_length=10)
    Nome_Mae = models.CharField(max_length=200)
    tituloeleitor= models.CharField(blank=True ,null=True , max_length=100)
    RG = models.CharField(blank=True ,null=True , max_length=15)
    ExpeditorRG = models.CharField (blank=True ,null=True , max_length=10)
    UF_RG = models.CharField(blank=True ,null=True , max_length=2)
    Nome_Fantasia = models.CharField(max_length=250)
    Capitao_Inicial = models.CharField(blank=True ,null=True , max_length=15)
    OcupacaoPrincipal = models.CharField(blank=True ,null=True , max_length=500)
    OcupacaoSegundario = models.TextField(blank=True ,null=True , max_length=500)
    formaatuacao = models.TextField(blank=True ,null=True,max_length=100)
    faturamento_anual = models.CharField(blank=True ,null=True,max_length=100)
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