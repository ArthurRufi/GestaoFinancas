from django.urls import path
from .views import ConsultarReceitasAPIView, AdicionarReceitaAPI

urlpatterns = [
    path('receitasdespesas/consultar/', ConsultarReceitasAPIView.as_view(), name='consultar_receitas'),
    path('adicionar/', AdicionarReceitaAPI.as_view(), name='adicionar-movimentacao')
]
