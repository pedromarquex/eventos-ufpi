from django.forms import ModelForm
from .models import Organizador


class OrganizadorForm(ModelForm):
    class Meta:
        model = Organizador
        fields = ['first_name', 'last_name', 'email']
