from django.db import models

class Acessoria(models.Model):

    choicesSimNao = (('S','Sim'),
                    ('N','Nao'))

    choicespCnai =(('0121101','Viveirista independente'),
                    ('0159801','Apicultor(a) independente'),
                    ('0159802','Criador(a) de animais domésticos independente')
    )

    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    CPF = models.IntegerField()
    telefone = models.IntegerField()
    RG = models.IntegerField()
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
    CEP = models.IntegerField()
    Rua = models.CharField(max_length=200)
    Numero = models.IntegerField()
    Complemento = models.CharField(max_length=50)
    Bairro = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome