# Generated by Django 4.0.3 on 2022-05-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0032_acessoria_cnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='acessoria',
            name='faturamento_anual',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
