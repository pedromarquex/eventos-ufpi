from django.urls import path
from .views import Index, EditarEvento

app_name = 'eventos'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('editar-evento', EditarEvento.as_view(), name='editar-evento'),
]
