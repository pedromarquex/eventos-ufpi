# Generated by Django 2.2.5 on 2020-03-03 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0007_auto_20200229_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patrocinador',
            name='evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eventos.Evento'),
        ),
    ]