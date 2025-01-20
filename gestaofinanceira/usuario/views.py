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
            # Verifica se o email já está registrado
            if User.objects.filter(userEmail=data.get('userEmail')).exists():
                return Response({"error": "Usuário com este email já existe!"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Valida os dados usando o serializer
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()  # Salva os dados no banco
                return Response({"message": "Usuário criado com sucesso!"}, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class EncontrarUsuario(APIView):
    def get(self, request, usuario):
        try:
            # Busca o usuário pelo nome
            usuarioEntregue = User.objects.get(name=usuario)

            # Serializa e retorna os dados
            serializer = UserSerializer(usuarioEntregue)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response(
                {"Alert Message": "Usuário não encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )
