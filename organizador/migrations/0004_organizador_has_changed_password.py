# Generated by Django 3.0.4 on 2020-05-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizador', '0003_remove_organizador_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizador',
            name='has_changed_password',
            field=models.BooleanField(default=False),
        ),
    ]
