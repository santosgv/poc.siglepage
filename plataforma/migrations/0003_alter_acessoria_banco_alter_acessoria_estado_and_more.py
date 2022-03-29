# Generated by Django 4.0.3 on 2022-03-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0002_rename_cnpj_acessoria_cep_acessoria_bairro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessoria',
            name='Banco',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='acessoria',
            name='Estado',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='acessoria',
            name='Imposto',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='acessoria',
            name='OcupacaoPrincipal',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='acessoria',
            name='OcupacaoSegundario',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='acessoria',
            name='UF_RG',
            field=models.CharField(max_length=2),
        ),
    ]