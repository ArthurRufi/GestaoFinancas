from django.urls import path
from .views import ConsultarReceitasAPIView, AdicionarReceitaAPI,  AdiconarDesepesaAPIView, ConsultarDespesasAPIView

urlpatterns = [
    path('consultar/receita', ConsultarReceitasAPIView.as_view(), name='consultar_receitas'),
    path('adicionar/receita/', AdicionarReceitaAPI.as_view(), name='adicionar-movimentacao'),
    path('adicionar/despesa/', AdiconarDesepesaAPIView.as_view(), name='adicionar-despesas'),
    path('consultar/despesas')
]
