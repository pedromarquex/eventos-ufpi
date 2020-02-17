from django.urls import path
from .views import Index, EditarEventoInfo

app_name = 'eventos'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<slug:slug>/editar-info', EditarEventoInfo.as_view(), name='editar-evento-info'),
]
