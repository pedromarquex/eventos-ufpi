# Generated by Django 3.0.6 on 2020-06-27 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0014_auto_20200623_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palestrante',
            name='atividade',
        ),
        migrations.RemoveField(
            model_name='palestrante',
            name='link',
        ),
        migrations.AddField(
            model_name='atividade',
            name='palestrante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eventos.Palestrante'),
        ),
        migrations.AddField(
            model_name='palestrante',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='palestrante',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='palestrante',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='palestrante',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apoiador',
            name='link',
            field=models.URLField(max_length=150),
        ),
        migrations.AlterField(
            model_name='palestrante',
            name='apresentacao',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='palestrante',
            name='resumo',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='patrocinador',
            name='link',
            field=models.URLField(max_length=150),
        ),
        migrations.AlterField(
            model_name='realizador',
            name='link',
            field=models.URLField(max_length=150),
        ),
    ]