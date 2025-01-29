from django.urls import path
from .views import ConsultasAPIView, AdicionarReceitaAPI,  AdiconarDesepesaAPIView

urlpatterns = [
    path('consultar/receita/', ConsultasAPIView.as_view(), name='consultar_receitas'),
    path('adicionar/receita/', AdicionarReceitaAPI.as_view(), name='adicionar-movimentacao'),
    path('adicionar/despesa/', AdiconarDesepesaAPIView.as_view(), name='adicionar-despesas'),
]
