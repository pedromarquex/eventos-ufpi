from django.urls import path
from .views import Index, EditarEventoInfo, dias_atividades, NovaAtividade, EditarAtividade
from .views import palestrantes, NovoPalestrante, EditarPalestrante

app_name = 'eventos'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<slug:slug>/editar/info-contatos', EditarEventoInfo.as_view(), name='editar-info'),
    path('<slug:slug>/editar/dia/<int:dia>', dias_atividades, name='dias-atividades'),
    path('<slug:slug>/dia/<int:dia>/nova-atividade', NovaAtividade.as_view(),
         name='nova-atividade'),
    path('<slug:slug>/dia/<int:dia>/editar-atividade/<int:apk>', EditarAtividade.as_view(),
         name='editar-atividade'),
    path('<slug:slug>/palestrantes', palestrantes, name='palestrantes'),
    path('<slug:slug>/novo-palestrante', NovoPalestrante.as_view(), name='novo-palestrante'),
    path('<slug:slug>/editar-palestrante/<int:pk>', EditarPalestrante.as_view(), name='editar-palestrante'),
]
