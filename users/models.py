from django.db import models
from django.contrib.auth.models import User


class Administrador(models.Model):
    nome = models.CharField(max_length=150)
    foto = models.ImageField()
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Organizador(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
