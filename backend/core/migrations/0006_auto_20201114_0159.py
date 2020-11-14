# Generated by Django 3.1.3 on 2020-11-14 04:59

import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201114_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('sessao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sessao', verbose_name='Avaliacao_ID')),
                ('trabalho_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trabalho', verbose_name='Trabalho_ID')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
        migrations.AlterField(
            model_name='ano',
            name='ano',
            field=models.IntegerField(unique=True, validators=[core.validators.min_value_date, core.validators.max_value_date]),
        ),
        migrations.CreateModel(
            name='AvaliadorAvaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('avaliacao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.avaliacao', verbose_name='Avaliacao_ID')),
                ('avaliador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.avaliador', verbose_name='Avaliador_ID')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
