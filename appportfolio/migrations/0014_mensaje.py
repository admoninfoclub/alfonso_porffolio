# Generated by Django 4.1.5 on 2024-11-21 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appportfolio', '0013_alter_valoracion_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(verbose_name='Contenido del mensaje')),
                ('fecha_envio', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')),
                ('leido', models.BooleanField(default=False, verbose_name='Leído')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_recibidos', to=settings.AUTH_USER_MODEL)),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_enviados', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['fecha_envio'],
            },
        ),
    ]
