from django.db import models


class Acessoria(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    CPF = models.CharField(max_length=12)
    telefone = models.CharField(max_length=15)
    RG = models.CharField(max_length=15)
    ExpeditorRG = models.CharField(max_length=10)
    UF_RG = models.CharField(max_length=2)
    Data_Nascimento = models.CharField(max_length=10)
    Nome_Mae = models.CharField(max_length=200)
    Banco = models.CharField(max_length=1)
    Imposto = models.CharField(max_length=1)
    Nome_Fantasia = models.CharField(max_length=250)
    Capitao_Inicial = models.IntegerField()
    OcupacaoPrincipal = models.CharField(max_length=7)
    OcupacaoSegundario = models.CharField(max_length=7)
    CEP = models.CharField(max_length=15)
    Rua = models.CharField(max_length=200)
    Numero = models.IntegerField()
    Complemento = models.CharField(max_length=50)
    Bairro = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Estado = models.CharField(max_length=2)
    

    def __str__(self):
        return self.nome

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