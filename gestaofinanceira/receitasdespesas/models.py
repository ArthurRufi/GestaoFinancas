from django.db import models


class ReceitasDespesas(models.Model):
    #colocar na documentação 1 = Receita, 2 = Despesas
    tipo = models.IntegerField(default=2)
    valor = models.FloatField(default=0.0)
    dataDaMovimentacao = models.DateTimeField()
    descrição = models.CharField()


