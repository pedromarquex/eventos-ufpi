from django.forms import ModelForm
from .models import Evento, Dia, MicroEvento, Palestrante
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


class DiaForm(ModelForm):
    class Meta:
        model = Dia
        fields = '__all__'


class MicroEventoForm(ModelForm):
    class Meta:
        model = MicroEvento
        fields = '__all__'


class PalestranteForm(ModelForm):
    class Meta:
        model = Palestrante
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
