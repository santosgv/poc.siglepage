# Generated by Django 4.0.3 on 2022-04-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0020_alter_acessoria_cep_alter_acessoria_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessoria',
            name='Capitao_Inicial',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='acessoria',
            name='Numero',
            field=models.CharField(max_length=5),
        ),
    ]
