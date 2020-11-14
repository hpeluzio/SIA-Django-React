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
    ano = models.IntegerField(unique=True, validators=[atual_year_not_past])

    def __str__(self):
        return r'Ano: {self.ano}'


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
    departamento_id = models.ForeignKey(Departamento, on_delete=models.CASCADE)
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
    departamento_id = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    ano_id = models.ForeignKey(Ano, on_delete=models.CASCADE)

    def __str__(self):
        return r'TRABALHO_ID: {self.trabalho_id}'


class TrabalhoAutor(Base):
    trabalho_id = models.ForeignKey(Trabalho, on_delete=models.CASCADE)
    autor = models.CharField('Autor', max_length=254)

    class Meta:
        verbose_name = 'Trabalhoautor'
        verbose_name_plural = 'Trabalhoautores'

    def __str__(self):
        return r'Autor: {self.autor}'
