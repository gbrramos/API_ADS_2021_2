# Generated by Django 3.2.4 on 2021-11-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuadroPresenca', '0004_auto_20211008_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='quadropresenca',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]