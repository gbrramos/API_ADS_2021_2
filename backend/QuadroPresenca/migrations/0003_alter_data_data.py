# Generated by Django 3.2.4 on 2021-10-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuadroPresenca', '0002_auto_20211004_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
