from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from usuario.utils.emailverify import Verify
from .models import User
from .serializers import UserSerializer

class CadastrarUsuario(APIView):
    def post(self, request):
        data = request.data
        try:
            # Verifica se o email já está registrado
            if not Verify(data.get('userEmail')).validar_email():
                return Response({"error": "ERROR EMAIL VALIDATION: ALGO DE ERRADO COM SEU EMAIL: "}, status=status.HTTP_400_BAD_REQUEST)
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
            # Busca múltiplos usuários pelo nome
            users = User.objects.filter(userEmail=usuario)

            if not users.exists():
                return Response({"error": "Nenhum usuário encontrado."}, status=status.HTTP_404_NOT_FOUND)

            # Serializa os resultados
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # Retorna erro caso ocorra alguma exceção
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class ApagarUsuario(APIView):
    def delete(self, request):
        name = request.data.get('name')
        userEmail = request.data.get('userEmail')
        dataDeNascimento = request.data.get('dataDeNascimento')
        senhaUser = request.data.get('senhaUser')

        if not all([name, userEmail, senhaUser]):  # Verifica se todos os campos obrigatórios foram enviados
            return Response({"ERROR": "Todos os campos obrigatórios devem ser preenchidos!"}, status=status.HTTP_400_BAD_REQUEST)

        # Busca o usuário no banco
        user = get_object_or_404(User, name=name, userEmail=userEmail)

        # Valida a senha
        if user.senhaUser != senhaUser:  # Comparação direta (não recomendado para senhas seguras)
            return Response({"ERROR": "Senha incorreta!"}, status=status.HTTP_403_FORBIDDEN)


        # Deleta o usuário
        user.delete()
        return Response({"message": "Usuário deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)

class ModificarUsuario(APIView):
    def patch(self, request):
        data = request.data  # Dados recebidos da requisição
        
        # Verifica se o usuário existe no banco pelo email
        user = User.objects.filter(userEmail=data.get('userEmail')).first()
        
        if not user:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        # Atualiza apenas os campos enviados na requisição
        serializer = UserSerializer(user, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)