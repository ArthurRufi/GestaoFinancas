from receitasdespesas.models import ReceitasDespesas
from rest_framework.serializers import Serializer


class GestaoRDSerializers(Serializer):
    class Meta:
        model = ReceitasDespesas
        fields = ['id', 'tipo', 'valor', 'dataDaMovimentacao', 'descricao', 'usuario_email']