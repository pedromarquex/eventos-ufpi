# Generated by Django 2.2.5 on 2020-03-03 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0008_auto_20200303_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apoiador',
            name='evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eventos.Evento'),
        ),
        migrations.AlterField(
            model_name='realizador',
            name='evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eventos.Evento'),
        ),
    ]
