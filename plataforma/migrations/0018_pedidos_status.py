# Generated by Django 4.0.3 on 2022-04-01 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0017_alter_produto_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='status',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
