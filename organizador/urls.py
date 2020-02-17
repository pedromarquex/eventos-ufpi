from django.urls import path

from organizador.views import meus_eventos

app_name = 'organizador'

urlpatterns = [
    path('meus-eventos', meus_eventos, name='meus-eventos'),
]
