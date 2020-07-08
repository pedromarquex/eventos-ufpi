from django.urls import path

from .views import ListarOrganizador, NovoOrganizador, EditarOrganizador, excluir_organizador
from .views import ListaEventos, NovoEvento, EditarEvento, excluir_evento

app_name = 'administrador'

urlpatterns = [
    # Gerenciamento de Organizadores
    path('novo-organizador', NovoOrganizador.as_view(), name='novo-organizador'),
    path('listar-organizadores', ListarOrganizador.as_view(), name='listar-organizadores'),
    path('editar-organizador/<int:pk>', EditarOrganizador.as_view(), name='editar-organizador'),
    path('excluir-organizador/<int:pk>', excluir_organizador, name='excluir-organizador'),

    # Gerenciamento de Eventos
    path('listar-eventos', ListaEventos.as_view(), name='listar-eventos'),
    path('novo-evento', NovoEvento.as_view(), name='novo-evento'),
    path('editar-evento/<int:pk>', EditarEvento.as_view(), name='editar-evento'),
    path('excluir-evento/<int:pk>', excluir_evento, name='excluir-evento'),
]
