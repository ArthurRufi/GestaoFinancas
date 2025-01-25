from datetime import datetime
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import ReceitasDespesas
from .serializers import ReceitaSerializer
import pytz

class ConsultarReceitasAPIView(APIView):
    def get(self, request):
        # Acessando os parâmetros da query string da URL
        dataInicio = request.query_params.get('dataInicio')
        dataFim = request.query_params.get('dataFim')
        usuario = request.query_params.get('usuario_email')
        tipo = request.query_params.get('tipo')

        # Verificando e convertendo as datas
        if dataInicio:
            try:
                # Convertendo para o formato datetime e aplicando o fuso horário UTC
                dataInicio = datetime.strptime(dataInicio, '%Y-%m-%d %H:%M:%S')
                dataInicio = pytz.utc.localize(dataInicio)  # Usa pytz para definir o fuso horário UTC
                print(dataInicio)
            except ValueError:
                return Response({"error": "Formato de dataInicio inválido. Use o formato YYYY-MM-DD HH:MM:SS."},
                                status=status.HTTP_400_BAD_REQUEST)

        if dataFim:
            try:
                # Convertendo para o formato datetime e aplicando o fuso horário UTC
                dataFim = datetime.strptime(dataFim, '%Y-%m-%d %H:%M:%S')
                dataFim = pytz.utc.localize(dataFim)  # Usa pytz para definir o fuso horário UTC
                print (dataFim)
            except ValueError:
                return Response({"error": "Formato de dataFim inválido. Use o formato YYYY-MM-DD HH:MM:SS."},
                                status=status.HTTP_400_BAD_REQUEST)

        if dataInicio and dataFim:
            try:
                # Filtrando as receitas/despesas no intervalo fornecido
                queryset = ReceitasDespesas.objects.filter(
                    dataDaMovimentacao__range=[dataInicio, dataFim]
                )
                
                # Filtrando também por usuário e tipo, caso esses parâmetros sejam passados
                if usuario:
                    queryset = queryset.filter(usuario_email=usuario)
                    print(f"Query Params: {request.query_params}")

                if tipo:
                    queryset = queryset.filter(tipo=tipo)

                # Serializar os resultados
                serializer = ReceitaSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(
                {"error": "Os campos 'dataInicio' e 'dataFim' são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST,
            )


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