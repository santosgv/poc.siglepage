# Generated by Django 4.0.3 on 2022-04-27 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0023_acessoria_nome_impresarial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acessoria',
            name='formaatuacao1',
        ),
        migrations.RemoveField(
            model_name='acessoria',
            name='formaatuacao2',
        ),
        migrations.RemoveField(
            model_name='acessoria',
            name='formaatuacao3',
        ),
    ]
