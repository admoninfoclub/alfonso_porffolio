# Generated by Django 4.1.5 on 2023-02-13 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expe_categoria', to='appportfolio.categoria'),
        ),
    ]
