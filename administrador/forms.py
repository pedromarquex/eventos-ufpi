from django.forms import ModelForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User

from eventos.models import Evento


class CustomUsernameForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']
        field_classes = {'username': UsernameField}


class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'organizador']
