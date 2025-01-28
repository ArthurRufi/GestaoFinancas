from django.db import models


class ReceitasDespesas(models.Model):
    #colocar na documentação 1 = Receita, 2 = Despesas
    tipo = models.IntegerField(default=2)
    valor = models.FloatField(default=0.0)
    dataDaMovimentacao = models.DateTimeField()
    descricao = models.CharField(max_length=500)
    usuario_email = models.EmailField()


class InforTratadas(models.Model):
    pass

