# Generated by Django 4.0.3 on 2022-03-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_alter_acessoria_banco_alter_acessoria_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessoria',
            name='Data_Nascimento',
            field=models.CharField(max_length=10),
        ),
    ]
