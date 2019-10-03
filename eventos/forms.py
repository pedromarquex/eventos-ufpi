from django.forms import ModelForm
from .models import *


class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'


class ApresentacaoForm(ModelForm):
    class Meta:
        model = Apresentacao
        fields = '__all__'


class ProgramacaoForm(ModelForm):
    class Meta:
        model = Programacao
        fields = '__all__'


class MicroEventoForm(ModelForm):
    class Meta:
        model = MicroEvento
        fields = '__all__'


class PatrocinadorForm(ModelForm):
    class Meta:
        model = Patrocinador
        fields = '__all__'


class RealizadorForm(ModelForm):
    class Meta:
        model = Realizador
        fields = '__all__'


class ApoiadorForm(ModelForm):
    class Meta:
        model = Apoiador
        fields = '__all__'
