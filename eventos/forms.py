from django.forms import ModelForm, FileInput, Select
from .models import Evento, Dia, Atividade, Palestrante
from .models import Patrocinador, Realizador, Apoiador


class EventoAdminForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'organizador']


class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        exclude = ['nome', 'organizador', 'slug', 'is_active']
        widgets = {
            'banner': FileInput(),
        }


class DiaForm(ModelForm):
    class Meta:
        model = Dia
        fields = '__all__'
        exclude = ['evento']


class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = '__all__'
        exclude = ['dia']


class PalestranteForm(ModelForm):
    class Meta:
        model = Palestrante
        fields = '__all__'
        exclude = ['evento', 'atividade']
        widgets = {
            'foto': FileInput()
        }


class PatrocinadorForm(ModelForm):
    class Meta:
        model = Patrocinador
        fields = '__all__'
        exclude = ['evento']
        widgets = {
            'foto': FileInput()
        }


class RealizadorForm(ModelForm):
    class Meta:
        model = Realizador
        fields = '__all__'
        exclude = ['evento']
        widgets = {
            'foto': FileInput()
        }


class ApoiadorForm(ModelForm):
    class Meta:
        model = Apoiador
        fields = '__all__'
        exclude = ['evento']
        widgets = {
            'foto': FileInput()
        }
