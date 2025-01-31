from django.db import models
from datetime import date

#vai receber alertas no dia sobre transações 
class DiaComGastosExorbitantes(models.Model):
    diaDasTransacoes = models.DateField(default=date.today)
    descricaoDaTransacao = models.CharField()
    emailUsuarioTransacao = models.EmailField()
    quantidadeDeTrasacoes = models.IntegerField()
    valoresTotais = models.FloatField()

