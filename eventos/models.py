from django.db import models
from django.template.defaultfilters import slugify
from core.models import Organizador


class Apresentacao(models.Model):
    realizacao = models.CharField(max_length=150)
    texto_apresentacao = models.TextField(max_length=300)


class Evento(models.Model):
    # básicas
    banner = models.ImageField(blank=True, null=True)
    nome = models.CharField(max_length=150)
    sobre = models.TextField()
    onde = models.CharField(200)
    quando = models.CharField(200)

    # contato
    endereco = models.CharField(200)
    telefone = models.CharField(20)
    email = models.EmailField()

    organizador = models.OneToOneField(Organizador, on_delete=models.SET_NULL)

    slug = models.SlugField(blank=True, null=True)
    apresentecao = models.OneToOneField(Apresentacao, null=True, blank=True, on_delete=models.SET_NULL)

    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)

        super(Evento, self).save(*args, **kwargs)


class Programacao(models.Model):
    dia = models.IntegerField()
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL)

    def __str__(self):
        return "dia " + str(self.dia)


class MicroEvento(models.Model):
    nome = models.CharField(max_length=150)
    horario = models.TimeField()
    local = models.CharField(max_length=300)
    programacao = models.ForeignKey(Programacao, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome


class Palestrante(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='perfil/palestrante', null=True, blank=True)
    resumo = models.CharField(max_length=200)
    apresentacao = models.TextField()

    microevento = models.ForeignKey(MicroEvento, on_delete=models.SET_NULL)


class Patrocinador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    evento = models.OneToOneField(Evento, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome


class Realizador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    evento = models.OneToOneField(Evento, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome


class Apoiador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    evento = models.OneToOneField(Evento, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome
