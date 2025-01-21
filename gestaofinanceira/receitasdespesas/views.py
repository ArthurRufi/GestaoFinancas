from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import ReceitasDespesas
from .serializers import ReceitaSerializer



class ConsultarReceitasAPIView(APIView):
    def get(self, request):
        user_id = request.data.get('user_id')
        tipo = request.data.get('tipo')

        if not user_id or not tipo:
            return Response(
                {"error": "Os parâmetros 'user_id' e 'tipo' são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            tipo = int(tipo)
        except ValueError:
            return Response(
                {"error": "'tipo' deve ser um número inteiro."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        movimentacoes = ReceitasDespesas.objects.filter(usuario_id=user_id, tipo=tipo)

        # Se não houver registros, retornar uma resposta adequada
        if not movimentacoes.exists():
            return Response(
                {"message": "Nenhuma movimentação encontrada."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Serializar os dados filtrados
        serializer = ReceitaSerializer(movimentacoes, many=True)

        # Retornar a resposta com os dados serializados
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class AdicionarReceitaAPI(APIView):
    def post(self, request, *args, **kwargs):
        # O serializer recebe os dados da requisição
        serializer = ReceitaSerializer(data=request.data)
        
        # Verifica se os dados passados são válidos
        if serializer.is_valid():
            # Salva os dados no banco de dados
            serializer.save()

            # Retorna os dados criados com status HTTP 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Se os dados não forem válidos, retorna os erros com status HTTP 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
