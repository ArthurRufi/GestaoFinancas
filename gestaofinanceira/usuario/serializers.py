from rest_framework import serializers
from usuario.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'userEmail', 'dataDeNascimento', 'senhaUser']
