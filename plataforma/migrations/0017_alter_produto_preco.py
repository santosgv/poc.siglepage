# Generated by Django 4.0.3 on 2022-04-01 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0016_remove_pedidos_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.FloatField(max_length=5),
        ),
    ]