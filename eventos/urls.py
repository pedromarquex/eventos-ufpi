from django.urls import path
from .views import Index
from .views import EditarEventoInfo
from .views import dias_atividades, NovaAtividade, EditarAtividade
from .views import palestrantes, NovoPalestrante, EditarPalestrante
from .views import patrocinadores, NovoPatrocinador, EditarPatrocinador

app_name = 'eventos'

urlpatterns = [
    # Listagem de todos os eventos
    path('', Index.as_view(), name='index'),

    # EDIÇÃO DE EVENTOS
    # info e contatos
    path('<slug:slug>/editar/info-contatos', EditarEventoInfo.as_view(), name='editar-info'),

    # dias de evento e atividades
    path('<slug:slug>/editar/dia/<int:dia>', dias_atividades, name='dias-atividades'),
    path('<slug:slug>/dia/<int:dia>/nova-atividade', NovaAtividade.as_view(),
         name='nova-atividade'),
    path('<slug:slug>/dia/<int:dia>/editar-atividade/<int:apk>', EditarAtividade.as_view(),
         name='editar-atividade'),

    # palestrantes
    path('<slug:slug>/palestrantes', palestrantes, name='palestrantes'),
    path('<slug:slug>/novo-palestrante', NovoPalestrante.as_view(), name='novo-palestrante'),
    path('<slug:slug>/editar-palestrante/<int:pk>', EditarPalestrante.as_view(), name='editar-palestrante'),

    # patrocinadores
    path('<slug:slug>/patrocinadores', patrocinadores, name='patrocinadores'),
    path('<slug:slug>/novo-patrocinador', NovoPatrocinador.as_view(), name='novo-patrocinador'),
    path('<slug:slug>/editar-patrocinador/<int:pk>', EditarPatrocinador.as_view(), name='editar-patrocinador'),
]
