from django.contrib.auth.models import User
from django.db import models


class Organizador(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    full_name = models.CharField(max_length=160, null=True, blank=True)
    # foto = models.ImageField(upload_to='perfil/organizador', null=True, blank=True)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    has_changed_password = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.full_name = "{} {}".format(self.first_name, self.last_name)

        super(Organizador, self).save(*args, **kwargs)
