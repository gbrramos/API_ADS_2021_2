# Generated by Django 3.2.7 on 2021-09-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Colaboradores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='dataDemissao',
            field=models.DateField(null=True),
        ),
    ]
