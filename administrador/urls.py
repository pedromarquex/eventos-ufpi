from django.urls import path

from administrador.views import ListarOrganizador, NovoOrganizador, EditarOrganizador

app_name = 'administrador'

urlpatterns = [
    path('novo-organizador', NovoOrganizador.as_view(), name='novo-organizador'),
    path('listar-organizadores', ListarOrganizador.as_view(), name='listar-organizadores'),
    path('editar-organizador', EditarOrganizador.as_view(), name='editar-organizador'),
]
