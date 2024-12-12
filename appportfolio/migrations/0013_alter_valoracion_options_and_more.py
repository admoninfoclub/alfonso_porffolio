# Generated by Django 4.1.5 on 2024-11-19 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0012_valoracion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='valoracion',
            options={},
        ),
        migrations.RemoveField(
            model_name='valoracion',
            name='entrevistador',
        ),
        migrations.AlterField(
            model_name='valoracion',
            name='media_aspectos',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Media Aspectos'),
        ),
        migrations.AlterField(
            model_name='valoracion',
            name='votos_empresa',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Votos Empresa'),
        ),
        migrations.AlterField(
            model_name='valoracion',
            name='votos_entrevista',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Votos Entrevista'),
        ),
    ]