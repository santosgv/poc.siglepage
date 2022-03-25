from django.db import models

class Acessoria(models.Model):

    choices = (('MG', 'Minas Gerais'),
               ('SP', 'Sao Paulo'))

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
    UF_RG = models.CharField(max_length=2, choices=choices)
    Data_Nascimento = models.IntegerField()
    Nome_Mae = models.CharField(max_length=200)
    Banco = models.CharField(max_length=1, choices=choicesSimNao)
    Imposto = models.CharField(max_length=1, choices=choicesSimNao)
    Nome_Fantasia = models.CharField(max_length=250)
    Capitao_Inicial = models.IntegerField()
    OcupacaoPrincipal = models.CharField(max_length=7, choices=choicespCnai)
    OcupacaoSegundario = models.CharField(max_length=7, choices=choicespCnai)
    CEP = models.IntegerField()
    Rua = models.CharField(max_length=200)
    Numero = models.IntegerField()
    Complemento = models.CharField(max_length=50)
    Bairro = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Estado = models.CharField(max_length=2, choices=choices)

    def __str__(self):
        return self.nome