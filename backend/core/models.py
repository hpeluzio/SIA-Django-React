from django.db import models

from django.contrib.auth.models import User

from core.validators import *


class Base(models.Model):
    created_at = models.DateField('Data de criação', auto_now_add=True)
    updated_at = models.DateField('Data de atualização', auto_now=True)

    class Meta:
        abstract = True


class Departamento(Base):
    nome = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nome


class Ano(Base):
    ano = models.IntegerField(unique=True, validators=[
                              min_value_date, max_value_date])

    def __str__(self):
        return f'{self.ano}'


class Sala(Base):
    TIPO = (
        ('P', 'Painel'),
        ('O', 'Oral')
    )
    nome = models.CharField('Nome', max_length=64)
    descricao = models.CharField('Descriçao', max_length=254)
    capacidade = models.PositiveIntegerField('Capacidade')
    tipo = models.CharField('Tipo', max_length=1, choices=TIPO)

    def __str__(self):
        return self.nome


class Avaliador(Base):
    nome = models.CharField('Nome', max_length=254)
    matricula = models.CharField('Matrícula', max_length=10)
    curso = models.CharField('Curso', max_length=254)
    departamento_id = models.ForeignKey(
        Departamento, verbose_name='Departamento_ID', on_delete=models.CASCADE)
    email = models.EmailField('E-mail', max_length=254)
    ativo = models.BooleanField('Ativo?', default=False)

    class Meta:
        verbose_name = 'Avaliador'
        verbose_name_plural = 'Avaliadores'

    def __str__(self):
        return self.nome


class Trabalho(Base):
    trabalho_id = models.IntegerField('TRABALHO_ID', unique=True)
    nome = models.CharField('Nome', max_length=254)
    orientador = models.CharField('Orientador', max_length=254)
    modalidade = models.CharField('Modalidade', max_length=254)
    area = models.CharField('Área', max_length=254)
    departamento_id = models.ForeignKey(
        Departamento, verbose_name='Departamento_ID', on_delete=models.CASCADE)
    ano_id = models.ForeignKey(
        Ano, verbose_name='Ano_ID', on_delete=models.CASCADE)

    def __str__(self):
        return f'TRABALHO_ID: {self.trabalho_id}'


class TrabalhoAutor(Base):
    trabalho_id = models.ForeignKey(
        Trabalho, verbose_name='Trabalho_ID', on_delete=models.CASCADE)
    autor = models.CharField('Autor', max_length=254)

    class Meta:
        verbose_name = 'Trabalho - Autor'
        verbose_name_plural = 'Trabalho - Autores'

    def __str__(self):
        return f'{self.autor}'


class Sessao(Base):
    TIPO = (
        ('P', 'Painel'),
        ('O', 'Oral')
    )
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    horario = models.TimeField('Horário', auto_now=False, auto_now_add=False)
    horariofim = models.TimeField(
        'Horário Fim', auto_now=False, auto_now_add=False)
    tipo = models.CharField('Tipo', max_length=1, choices=TIPO)
    departamento_id = models.ForeignKey(
        Departamento, verbose_name='Departamento_ID', on_delete=models.CASCADE)
    ano_id = models.ForeignKey(
        Ano, verbose_name='Ano_ID', on_delete=models.CASCADE)
    sala_id = models.ForeignKey(
        Sala, verbose_name='Sala_ID', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sessão'
        verbose_name_plural = 'Sessões'

    def __str__(self):
        return f'{self.data}'


class Avaliacao(Base):
    sessao_id = models.ForeignKey(
        Sessao, verbose_name='Avaliacao_ID', on_delete=models.CASCADE)
    trabalho_id = models.ForeignKey(
        Trabalho, verbose_name='Trabalho_ID', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f'Avaliação: {self.sessao_id} - {self.trabalho_id}'


class AvaliadorAvaliacao(Base):
    avaliador_id = models.ForeignKey(
        Avaliador, verbose_name='Avaliador_ID', on_delete=models.CASCADE)
    avaliacao_id = models.ForeignKey(
        Avaliacao, verbose_name='Avaliacao_ID', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Avaliador Avaliação'
        verbose_name_plural = 'Avaliadores - Avaliações'

    def __str__(self):
        return f'Avaliação: {self.avaliador_id} - {self.avaliacao_id}'
