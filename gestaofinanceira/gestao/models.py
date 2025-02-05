from django.db import models
from datetime import date

#vai receber alertas no dia sobre transações 
class DiaComGastosExorbitantes(models.Model):

    diaDasTransacoes = models.DateField(default=date.today)
    descricaoDaTransacao = models.CharField()
    emailUsuarioTransacao = models.EmailField()
    quantidadeDeTrasacoes = models.IntegerField()
    valoresTotais = models.FloatField()
    

class MetasFinanceiras(models.Model):
    diaInicial =  models.DateField(default=date.today)
    diaFinal = models.DateField()
    metaValor = models.FloatField()
    nomeDaMeta = models.CharField(max_length=255)
    quantidadeAtual = models.FloatField(default=0.0)