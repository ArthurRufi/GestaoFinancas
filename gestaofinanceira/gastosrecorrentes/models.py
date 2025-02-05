from django.db import models
from decimal import Decimal

class GastosRecorrentes(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição do Gasto")
    data_de_pagamento = models.DateField(verbose_name="Data de Pagamento")
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"), verbose_name="Valor")
    registro_de_importancia = models.PositiveIntegerField(default=2, verbose_name="Nível de Importância")
    registro_de_pagamento = models.BooleanField(default=False, verbose_name="Pago")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    class Meta:
        verbose_name = "Gasto Recorrente"
        verbose_name_plural = "Gastos Recorrentes"
        ordering = ["-data_de_pagamento"]

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor} ({'Pago' if self.registro_de_pagamento else 'Pendente'})"
