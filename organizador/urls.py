from django.urls import path

from .views import meus_eventos
from .views import Perfil, Senha, NovaSenha

app_name = 'organizador'

urlpatterns = [
    path('meus-eventos', meus_eventos, name='meus-eventos'),
    path('perfil', Perfil.as_view(), name='perfil'),
    path('senha', Senha.as_view(), name='senha'),
    path('nova-senha', NovaSenha.as_view(), name='nova-senha'),
]
