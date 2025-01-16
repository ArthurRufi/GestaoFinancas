from django.db import models


class ContasUsuario(models.Model):
    emailUsuario = models.CharField(max_length=300)
    bancoUsuario = models.CharField(max_length=255)
    agenciaUsuario = models.IntegerField()
    contaUsuario =models.IntegerField()