# Generated by Django 3.1.3 on 2020-11-14 00:05

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ano',
            name='ano',
            field=models.IntegerField(unique=True, validators=[core.validators.atual_year_not_past]),
        ),
    ]
