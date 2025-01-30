from django.urls import path
from .views import CadastrarUsuario, EncontrarUsuario, ApagarUsuario, ModificarUsuario


urlpatterns = [
    path('criar/', CadastrarUsuario.as_view(), name='criarUsuario'),
    path('consultar/<str:usuario>/', EncontrarUsuario.as_view(), name='consultarUsuario'),
    path('deletar/', ApagarUsuario.as_view(), name='delete-user'),
    path('modificar/', ModificarUsuario.as_view(), name='modificar')
    
]
