from django.forms import ModelForm
from core.models import Organizador


class OrganizadorForm(ModelForm):
    class Meta:
        model = Organizador
        fields = '__all__'
        exclude = ['user', 'is_active']
