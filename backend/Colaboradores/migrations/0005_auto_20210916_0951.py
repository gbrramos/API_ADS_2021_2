# Generated by Django 3.2.4 on 2021-09-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Colaboradores', '0004_alter_colaborador_datademissao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='matricula',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='nomeCompleto',
            field=models.CharField(max_length=255),
        ),
    ]
