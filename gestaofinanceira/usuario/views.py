from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class CadastrarUsuario(APIView):
    def post(self, request):
        data = request.data
        try:
            user = User.objects.create(
                name=data.get('name'),
                userEmail=data.get('userEmail'),
                dataDeNascimento=data.get('dataDeNascimento'),
                senhaUser=data.get('senhaUser')
            )
            user.save()
            return Response({"message": "Usuário criado com sucesso!"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

class EncontrarUsuario(APIView):
    def get(self, request, usuario):
        # O parâmetro da URL já é o nome do usuário
        username = usuario

        # Tenta buscar o usuário pelo nome
        usuarioEntregue = User.objects.filter(name=username)

        if not usuarioEntregue.exists():
            return Response(
                {"Alert Message": "Usuário não encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Caso encontre, retorna as informações
        return Response(
            {
                "name": usuarioEntregue.first().name,
                "email": usuarioEntregue.first().userEmail,
                "dataDeNascimento": usuarioEntregue.first().dataDeNascimento,
            },
            status=status.HTTP_200_OK,
        )