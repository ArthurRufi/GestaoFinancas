from rest_framework import serializers
from contasbancarias.models import ContasUsuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContasUsuario
        fields = ['id', 'emailUsuario', 'bancoUsuario', 'agenciaUsuario', 'contaUsuario']
