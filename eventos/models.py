from django.db import models
from django.template.defaultfilters import slugify
from organizador.models import Organizador


class Evento(models.Model):
    """ Guarda as informações de um Evento """
    # informações básicas
    banner = models.ImageField(upload_to='eventos/banner', blank=True, null=True)
    nome = models.CharField(max_length=150)
    sobre = models.TextField(null=True, blank=True)
    onde = models.CharField(max_length=200, null=True, blank=True)
    quando = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=100)

    # ĩnformações de contato
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # organizador do evento
    organizador = models.ForeignKey(Organizador, on_delete=models.SET_NULL, null=True, blank=True)

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
    """ Dia de Evento, começando em 1 """
    dia = models.IntegerField()

    # Referência para um Evento
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "dia " + str(self.dia)


class Atividade(models.Model):
    """ Um micro evento corresponde à uma palestra, keynote,
     ou mesmo um acontecimento como início do credenciamento """

    # informações básicas

    # abertura, keynote, artigo, palestra, pausa, encerramento, etc...
    tipo = models.CharField(max_length=40, null=True, blank=True)
    nome = models.CharField(max_length=150, null=True, blank=True)
    horario = models.TimeField()
    resumo = models.TextField(null=True, blank=True)

    # referência para um Dia de Evento
    dia = models.ForeignKey(Dia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Palestrante(models.Model):
    """ Participante que será responsável por uma palestra
     no Evento. Não será autenticável """
    # informações básicas
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='perfil/palestrante', null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    resumo = models.CharField(max_length=200)
    apresentacao = models.TextField()

    # referência para uma Atividade
    atividade = models.ForeignKey(Atividade, on_delete=models.SET_NULL, null=True, blank=True)


class Patrocinador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    link = models.CharField(max_length=150, null=True, blank=True)
    evento = models.OneToOneField(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Realizador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    link = models.CharField(max_length=150, null=True, blank=True)
    evento = models.OneToOneField(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Apoiador(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=150)
    link = models.CharField(max_length=150, null=True, blank=True)
    evento = models.OneToOneField(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
