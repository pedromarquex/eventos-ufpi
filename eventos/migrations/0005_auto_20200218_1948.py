# Generated by Django 2.2.5 on 2020-02-18 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_evento_instagram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]