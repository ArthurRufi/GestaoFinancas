from django.urls import path
from .views import ConsultarReceitasAPIView, AdicionarReceitaAPI

urlpatterns = [
    path('movimentacoes/<str:usuario>/<str:email>/<str:detailDate>/', ConsultarReceitasAPIView.as_view(), name='filtrar-movimentacoes'),
    path('adicionar/', AdicionarReceitaAPI.as_view(), name='adicionar-movimentacao')
]
