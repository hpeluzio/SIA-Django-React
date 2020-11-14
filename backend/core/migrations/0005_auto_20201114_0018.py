# Generated by Django 3.1.3 on 2020-11-14 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_trabalhoautor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliador',
            name='departamento_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.departamento', verbose_name='Departamento_ID'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='ano_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ano', verbose_name='Ano_ID'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='departamento_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.departamento', verbose_name='Departamento_ID'),
        ),
        migrations.AlterField(
            model_name='trabalhoautor',
            name='trabalho_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trabalho', verbose_name='Trabalho_ID'),
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
                ('ano_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ano', verbose_name='Ano_ID')),
                ('departamento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.departamento', verbose_name='Departamento_ID')),
                ('sala_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sala', verbose_name='Sala_ID')),
            ],
            options={
                'verbose_name': 'Sessão',
                'verbose_name_plural': 'Sessões',
            },
        ),
    ]