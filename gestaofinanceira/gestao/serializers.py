from receitasdespesas.models import ReceitasDespesas
from .models import DiaComGastosExorbitantes, MetasFinanceiras
from rest_framework.serializers import Serializer



class GestaoRDSerializers(Serializer):
    class Meta:
        model = ReceitasDespesas
        fields = ['id', 'tipo', 'valor', 'dataDaMovimentacao', 'descricao', 'usuario_email']



class DCGESerializer(Serializer):
    class Meta:
        model = DiaComGastosExorbitantes
        fields = ['id', 'diaDasTransacoes', 'descricaoDaTransacao',
                  'quantidadeDeTransacao', 'valoresTotais', 'emailUsuarioTransacao']
        

class MetasFinancasSerializers(Serializer):
    class Meta:
        models = MetasFinanceiras
        fields = ['diaInicial', 'diaFinal', 'metaValor',
                  'nomeDaMeta', 'quantidadeAtual']