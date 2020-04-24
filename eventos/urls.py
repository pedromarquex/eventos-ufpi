from django.urls import path
from .views import Index
from .views import EditarEventoInfo
from .views import dias_atividades, NovaAtividade, EditarAtividade, exclui_atividade, NovoDia, EditarDia, exclui_dia
from .views import palestrantes, NovoPalestrante, EditarPalestrante, exclui_palestrante
from .views import patrocinadores, NovoPatrocinador, EditarPatrocinador, exclui_patrocinador
from .views import realizadores, NovoRealizador, EditarRealizador, exclui_realizador
from .views import apoiadores, NovoApoiador, EditarApoiador, exclui_apoiador
from .views import evento

app_name = 'eventos'

urlpatterns = [
    # Listagem de todos os eventos
    path('', Index.as_view(), name='index'),

    # EDIÇÃO DE EVENTOS
    # info e contatos
    path('<slug:slug>/editar/info-contatos', EditarEventoInfo.as_view(), name='editar-info'),

    # dias de evento e atividades
    path('<slug:slug>/editar/dia/<int:dia>', dias_atividades, name='dias-atividades'),
    path('<slug:slug>/novo-dia', NovoDia.as_view(), name='novo-dia'),
    path('<slug:slug>/editar-dia/<int:pk>', EditarDia.as_view(), name='editar-dia'),
    path('<slug:slug>/dia/<int:pk>/excluir', exclui_dia, name='excluir-dia'),
    path('<slug:slug>/dia/<int:dia>/nova-atividade', NovaAtividade.as_view(),
         name='nova-atividade'),
    path('<slug:slug>/dia/<int:dia>/editar-atividade/<int:apk>', EditarAtividade.as_view(),
         name='editar-atividade'),
    path('<slug:slug>/dia/<int:dia>/atividades/<int:pk>/excluir', exclui_atividade, name='exclui-atividade'),

    # palestrantes
    path('<slug:slug>/palestrantes', palestrantes, name='palestrantes'),
    path('<slug:slug>/novo-palestrante', NovoPalestrante.as_view(), name='novo-palestrante'),
    path('<slug:slug>/editar-palestrante/<int:pk>', EditarPalestrante.as_view(), name='editar-palestrante'),
    path('<slug:slug>/palestrantes/<int:pk>/excluir', exclui_palestrante, name='excluir-palestrante'),

    # patrocinadores
    path('<slug:slug>/patrocinadores', patrocinadores, name='patrocinadores'),
    path('<slug:slug>/novo-patrocinador', NovoPatrocinador.as_view(), name='novo-patrocinador'),
    path('<slug:slug>/editar-patrocinador/<int:pk>', EditarPatrocinador.as_view(), name='editar-patrocinador'),
    path('<slug:slug>/patrocinadores/<int:pk>/excluir', exclui_patrocinador, name='excluir-patrocinador'),

    # realizadores
    path('<slug:slug>/realizadores', realizadores, name='realizadores'),
    path('<slug:slug>/novo-realizador', NovoRealizador.as_view(), name='novo-realizador'),
    path('<slug:slug>/editar-realizador/<int:pk>', EditarRealizador.as_view(), name='editar-realizador'),
    path('<slug:slug>/realizadores/<int:pk>/excluir', exclui_realizador, name='excluir-realizador'),

    # apoiadores
    path('<slug:slug>/apoiadores', apoiadores, name='apoiadores'),
    path('<slug:slug>/novo-apoiador', NovoApoiador.as_view(), name='novo-apoiador'),
    path('<slug:slug>/editar-apoiador/<int:pk>', EditarApoiador.as_view(), name='editar-apoiador'),
    path('<slug:slug>/apoiadores/<int:pk>/excluir', exclui_apoiador, name='excluir-apoiador'),

    # evento
    path('<slug:slug>/', evento, name='evento'),
]
