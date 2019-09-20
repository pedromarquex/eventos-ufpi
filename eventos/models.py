from django.db import models
from django.template.defaultfilters import slugify
from users.models import Organizador


class Apresentacao(models.Model):
    realizador = models.CharField(max_length=150)
    texto_apresentacao = models.TextField(max_length=300)


class Programacao(models.Model):
    dia = models.IntegerField()


class MicroEvento(models.Model):
    nome = models.CharField(max_length=150)
    horario = models.TimeField()
    local = models.CharField(max_length=300)
    programacao = models.ForeignKey(Programacao, on_delete=models.CASCADE)


class Evento(models.Model):
    nome = models.CharField(max_length=150)
    organizador = models.OneToOneField(Organizador, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    img1 = models.ImageField(blank=True, null=True)
    img2 = models.ImageField(blank=True, null=True)
    img3 = models.ImageField(blank=True, null=True)
    apresentecao = models.OneToOneField(Apresentacao, null=True, blank=True)
    programacao = models.OneToOneField(Programacao, null=True, blank=True)
    is_valid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.nome)

        super(Evento, self).save(*args, **kwargs)


class Patrocinador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)


class Realizador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)


class Apoiador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
