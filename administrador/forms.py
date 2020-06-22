from django.forms import ModelForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User


class CustomUsernameForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']
        field_classes = {'username': UsernameField}
