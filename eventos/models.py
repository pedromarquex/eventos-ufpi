from django.db import models
from django.template.defaultfilters import slugify
from core.models import Organizador


class Apresentacao(models.Model):
    realizacao = models.CharField(max_length=150)
    texto_apresentacao = models.TextField(max_length=300)


class Evento(models.Model):
    nome = models.CharField(max_length=150)
    organizador = models.OneToOneField(Organizador, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    img1 = models.ImageField(blank=True, null=True)
    img2 = models.ImageField(blank=True, null=True)
    img3 = models.ImageField(blank=True, null=True)
    apresentecao = models.OneToOneField(Apresentacao, null=True, blank=True, on_delete=models.CASCADE)

    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)

        super(Evento, self).save(*args, **kwargs)


class Programacao(models.Model):
    dia = models.IntegerField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return "dia " + str(self.dia)


class MicroEvento(models.Model):
    nome = models.CharField(max_length=150)
    horario = models.TimeField()
    local = models.CharField(max_length=300)
    programacao = models.ForeignKey(Programacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Patrocinador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Realizador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Apoiador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
