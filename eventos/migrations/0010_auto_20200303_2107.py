# Generated by Django 2.2.5 on 2020-03-04 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0009_auto_20200303_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
