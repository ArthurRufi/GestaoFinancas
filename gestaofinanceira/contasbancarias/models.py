from django.db import models


class ContasUsuario(models.Model):
    emailUsuario = models.CharField(max_length=300)
    bancoUsuario = models.CharField(max_length=255)
    agenciaUsuario = models.IntegerField()
    contaUsuario = models.IntegerField()
    '''
    
    #essa informações servirão para consulta simbolica
    #Em um futuro deve-se adicionar outro serviço somente para confirmação de CPF e etc, separando esse serviço do principal
    '''