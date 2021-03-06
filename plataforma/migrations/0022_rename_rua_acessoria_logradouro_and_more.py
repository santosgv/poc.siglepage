# Generated by Django 4.0.3 on 2022-04-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0021_alter_acessoria_capitao_inicial_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acessoria',
            old_name='Rua',
            new_name='logradouro',
        ),
        migrations.RemoveField(
            model_name='acessoria',
            name='Banco',
        ),
        migrations.RemoveField(
            model_name='acessoria',
            name='Imposto',
        ),
        migrations.AddField(
            model_name='acessoria',
            name='celular',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acessoria',
            name='email2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='formaatuacao',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='formaatuacao1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='formaatuacao2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='formaatuacao3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='logingov',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acessoria',
            name='nacionalidade',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acessoria',
            name='residencial_Bairro',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='residencial_CEP',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='residencial_Cidade',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='residencial_Complemento',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='residencial_Estado',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='residencial_Numero',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='residencial_logradouro',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='acessoria',
            name='senhagov',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acessoria',
            name='sexo',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acessoria',
            name='tituloeleitor',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acessoria',
            name='OcupacaoPrincipal',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='acessoria',
            name='OcupacaoSegundario',
            field=models.CharField(max_length=500),
        ),
    ]
