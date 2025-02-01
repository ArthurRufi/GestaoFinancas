from django.shortcuts import render
from rest_framework.views import APIView
from gestaofinanceira.gestao.utils.gerador_mensagens import EmailExcessiveSpending, EmailPasswordRecover
# Create your views here.


class ArtificialInteligenceForVicesAPI(APIView):
    
    #arquivo gerador para mini IA para explicar como anda os gastos pessoais
    pass


class situacaoFinanceira(APIView):
    #deve-se avisar o usuaio sobre sua situação fianceira atual
    #pegar gastos mensais e indicar prejuizo ou lucro
    pass
