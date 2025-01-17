from django.urls import path
from .views import CadastrarUsuario, EncontrarUsuario


urlpatterns = [
    path('criar/', CadastrarUsuario.as_view(), name='criarUsuario'),
    path('consultar/<str:usuario>/', EncontrarUsuario.as_view(), name='consultarUsuario'),
]
