from django.urls import path
from .views import Login, Logout, NovoOrganizador, ListarOrganizador

app_name = 'core'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('novo-organizador', NovoOrganizador.as_view(), name='novo-organizador'),
    path('listar-organizadores', ListarOrganizador.as_view(), name='listar-organizadores'),
]
