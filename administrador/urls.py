from django.urls import path

from administrador.views import ListarOrganizador, NovoOrganizador, EditarOrganizador
from .views import excluir_organizador

app_name = 'administrador'

urlpatterns = [
    path('novo-organizador', NovoOrganizador.as_view(), name='novo-organizador'),
    path('listar-organizadores', ListarOrganizador.as_view(), name='listar-organizadores'),
    path('editar-organizador/<int:pk>', EditarOrganizador.as_view(), name='editar-organizador'),
    path('excluir-organizador/<int:pk>', excluir_organizador, name='excluir-organizador'),
]
