from django.db import models


#Nos gastos recorrentes o django deve pegar os gastos que o usuario tem recorrentes e ir lembrando a ele de pagar

class GastosRecorrentes(models.Model):
    referenciaDoGasto = models.CharField(max_length=255)
    dataDePagamento = models.DateField()
    valor = models.FloatField()
    registroDeImportancia = models.IntegerField(default=2)
