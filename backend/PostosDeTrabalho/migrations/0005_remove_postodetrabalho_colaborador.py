# Generated by Django 3.2.7 on 2021-09-30 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PostosDeTrabalho', '0004_auto_20210929_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postodetrabalho',
            name='colaborador',
        ),
    ]
