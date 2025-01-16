from django.urls import path
from .views import CadastrarUsuario


urlpatterns = [
    path('criar/', CadastrarUsuario.as_view(), name='criarUsuario')
]
