# Generated by Django 3.2.7 on 2021-09-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostosDeTrabalho', '0003_postodetrabalho_colaborador'),
        ('Contratos', '0005_auto_20210918_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='postoDeTrabalho',
            field=models.ManyToManyField(to='PostosDeTrabalho.PostoDeTrabalho'),
        ),
    ]
