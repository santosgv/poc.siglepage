# Generated by Django 4.0.3 on 2022-03-29 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0005_produto_acessoria_preco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acessoria',
            name='preco',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
