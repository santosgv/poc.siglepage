# Generated by Django 4.0.3 on 2022-04-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0026_alter_acessoria_ocupacaosegundario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessoria',
            name='formaatuacao',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]