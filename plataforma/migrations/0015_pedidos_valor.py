# Generated by Django 4.0.3 on 2022-03-31 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0014_alter_produto_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='valor',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]