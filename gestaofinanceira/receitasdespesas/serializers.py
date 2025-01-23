from rest_framework import serializers
from receitasdespesas.models import ReceitasDespesas

    
class BaseRDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceitasDespesas
        fields = ['id', 'tipo', 'valor', 'dataDaMovimentacao', 'descricao', 'usuario_email']
    

class ReceitaSerializer(BaseRDSerializer):
    def validate_tipo(self, value):
        if value != 1:
            raise serializers.ValidationError("O tipo deve ser 1 para receitas.")
        return value
        

class DespesasSerializer(BaseRDSerializer):
    def validate_tipo(self, value):
        if value !=2:
            raise serializers.ValidationError("O tipo deve ser 2 para despesas")