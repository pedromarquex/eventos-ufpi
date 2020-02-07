from django.urls import path
from .views import Login, Logout, NovoOrganizador, ListarOrganizador, meus_eventos

app_name = 'core'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('novo-organizador', NovoOrganizador.as_view(), name='novo-organizador'),
    path('listar-organizadores', ListarOrganizador.as_view(), name='listar-organizadores'),
    path('meus-eventos', meus_eventos, name='meus-eventos'),
]
