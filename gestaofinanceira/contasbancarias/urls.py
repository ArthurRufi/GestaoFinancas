from django.urls import path
from .views import consultarConta
urlpatterns = [
    path("consultar/informacoes", consultarConta.as_view(), name="consultaSimples")
]
