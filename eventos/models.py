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
    instagram = models.CharField(max_length=100, null=True, blank=True)

    # ĩnformações de contato
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # organizador do evento
    organizador = models.ForeignKey(Organizador, on_delete=models.SET_NULL, null=True, blank=True)

    # slug gerado automaticamente, hidden no formulário
    slug = models.SlugField(unique=True, blank=True, null=True)

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
    data = models.CharField(max_length=15, null=True, blank=True)

    # Referência para um Evento
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.dia)


class Palestrante(models.Model):
    """ Participante que será responsável por uma palestra
     no Evento. Não será autenticável """
    # informações básicas
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='perfil/palestrante', null=True, blank=True, default='perfil/default.png')
    resumo = models.TextField(max_length=150, null=True, blank=True)
    apresentacao = models.TextField(max_length=500, null=True, blank=True)

    # contatos
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # referência para um Evento
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    """ Uma atividade corresponde à uma palestra, keynote,
     ou mesmo um acontecimento como início do credenciamento """

    # informações básicas

    # abertura, keynote, artigo, palestra, pausa, encerramento, etc...
    tipo = models.CharField(max_length=40, null=True, blank=True)
    nome = models.CharField(max_length=150, null=True, blank=True)
    horario = models.CharField(max_length=8, null=True, blank=True)
    resumo = models.TextField(null=True, blank=True)

    # referência para um Dia de Evento
    dia = models.ForeignKey(Dia, on_delete=models.SET_NULL, null=True, blank=True)

    # referencia do Palestrante responsável, se houver
    palestrante = models.ForeignKey(Palestrante, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Patrocinador(models.Model):
    foto = models.ImageField(upload_to="patrocinadores/banner")
    nome = models.CharField(max_length=150)
    link = models.URLField(max_length=150)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Realizador(models.Model):
    foto = models.ImageField(upload_to="realizadores/banner")
    nome = models.CharField(max_length=150)
    link = models.URLField(max_length=150)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Apoiador(models.Model):
    foto = models.ImageField(upload_to="apoiadores/banner")
    nome = models.CharField(max_length=150)
    link = models.URLField(max_length=150)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
