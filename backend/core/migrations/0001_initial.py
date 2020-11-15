# Generated by Django 3.1.3 on 2020-11-14 23:38

import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('ano', models.IntegerField(unique=True, validators=[core.validators.min_value_date, core.validators.max_value_date])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('nome', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=254, verbose_name='Descriçao')),
                ('capacidade', models.PositiveIntegerField(verbose_name='Capacidade')),
                ('tipo', models.CharField(choices=[('P', 'Painel'), ('O', 'Oral')], max_length=1, verbose_name='Tipo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('trabalho_id', models.IntegerField(unique=True, verbose_name='TRABALHO_ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome')),
                ('orientador', models.CharField(max_length=254, verbose_name='Orientador')),
                ('modalidade', models.CharField(max_length=254, verbose_name='Modalidade')),
                ('area', models.CharField(max_length=254, verbose_name='Área')),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ano', verbose_name='Ano')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.departamento', verbose_name='Departamento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrabalhoAutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('autor', models.CharField(max_length=254, verbose_name='Autor')),
                ('trabalho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trabalho', verbose_name='Trabalho')),
            ],
            options={
                'verbose_name': 'Trabalho - Autor',
                'verbose_name_plural': 'Trabalho - Autores',
            },
        ),
        migrations.CreateModel(
            name='Sessao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('data', models.DateField(verbose_name='Data')),
                ('horario', models.TimeField(verbose_name='Horário')),
                ('horariofim', models.TimeField(verbose_name='Horário Fim')),
                ('tipo', models.CharField(choices=[('P', 'Painel'), ('O', 'Oral')], max_length=1, verbose_name='Tipo')),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ano', verbose_name='Ano')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.departamento', verbose_name='Departamento')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sala', verbose_name='Sala')),
            ],
            options={
                'verbose_name': 'Sessão',
                'verbose_name_plural': 'Sessões',
            },
        ),
        migrations.CreateModel(
            name='Avaliador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome')),
                ('matricula', models.CharField(max_length=10, verbose_name='Matrícula')),
                ('curso', models.CharField(max_length=254, verbose_name='Curso')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('ativo', models.BooleanField(default=False, verbose_name='Ativo?')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.departamento', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Avaliador',
                'verbose_name_plural': 'Avaliadores',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('avaliadores', models.ManyToManyField(to='core.Avaliador')),
                ('sessao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sessao', verbose_name='Sessao')),
                ('trabalho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trabalho', verbose_name='Trabalho')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
    ]
