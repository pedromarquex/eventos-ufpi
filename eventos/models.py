from django.db import models
from django.template.defaultfilters import slugify
from core.models import Organizador


class Evento(models.Model):
    # informações básicas
    banner = models.ImageField(upload_to='eventos/banner', blank=True, null=True)
    nome = models.CharField(max_length=150)
    sobre = models.TextField(null=True, blank=True)
    onde = models.CharField(max_length=200, null=True, blank=True)
    quando = models.CharField(max_length=200, null=True, blank=True)

    # ĩnformações de contato
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # organizador do evento
    organizador = models.OneToOneField(Organizador, on_delete=models.SET_NULL, null=True, blank=True)

    # slug gerado automaticamente, hidden no formulário
    slug = models.SlugField(blank=True, null=True)

    # campo indica se o evento está ativo
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)

        super(Evento, self).save(*args, **kwargs)


class Dia(models.Model):
    dia = models.IntegerField()
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "dia " + str(self.dia)


class MicroEvento(models.Model):
    nome = models.CharField(max_length=150)
    horario = models.TimeField()
    local = models.CharField(max_length=300)
    dia = models.ForeignKey(Dia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Palestrante(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='perfil/palestrante', null=True, blank=True)
    resumo = models.CharField(max_length=200)
    apresentacao = models.TextField()

    microevento = models.ForeignKey(MicroEvento, on_delete=models.SET_NULL, null=True, blank=True)


class Patrocinador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    evento = models.OneToOneField(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Realizador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    evento = models.OneToOneField(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Apoiador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    evento = models.OneToOneField(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
