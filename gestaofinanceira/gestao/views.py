from django.shortcuts import render
from rest_framework.views import APIView
from gestaofinanceira.gestao.utils.gerador_mensagens import EmailExcessiveSpending, EmailPasswordRecover
from gestaofinanceira.receitasdespesas.models import ReceitasDespesas

# Create your views here.


class ArtificialInteligenceForVicesAPI(APIView):
    
    #arquivo gerador para mini IA para explicar como anda os gastos pessoais
    pass


class situacaoFinanceira(APIView):
    #deve-se avisar o usuaio sobre sua situação fianceira atual
    #pegar gastos mensais e indicar prejuizo ou lucro
    def mesNegativado():
        #pegar no banco de dados as informações da conta e lançar se estar negativado
        pass
    def granaSobrando():
        #avisa se está com grana sobrando OBS: AVISAR SE SOBROU MAIS DE 20% DOS GANHOS MENSAIS
        pass
    def juntandoGrana():
        #avisar que falta depositar os valores para a meta
        pass
    

    pass
