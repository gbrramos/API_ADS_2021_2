# Generated by Django 3.2.4 on 2021-11-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuadroPresenca', '0006_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='quadropresenca',
            name='justificativa',
            field=models.TextField(blank=True, null=True),
        ),
    ]
