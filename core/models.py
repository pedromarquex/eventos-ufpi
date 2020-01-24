from django.db import models
from django.contrib.auth.models import User


class Administrador(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    foto = models.ImageField(upload_to='perfil/administrador', null=True, blank=True)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Organizador(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    foto = models.ImageField(upload_to='perfil/organizador', null=True, blank=True)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
