from django.contrib.auth.models import User, Group
from rest_framework import serializers

from core.models import (Departamento, Ano, Sala,
                         Avaliador, Trabalho, TrabalhoAutor,
                         Sessao, Avaliacao)


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class AnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ano
        fields = '__all__'


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'


class AvaliadorSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()

    class Meta:
        model = Avaliador
        fields = '__all__'


class TrabalhoAutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrabalhoAutor
        fields = '__all__'


class TrabalhoSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()
    autores = TrabalhoAutorSerializer(many=True)

    class Meta:
        model = Trabalho
        fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):

    trabalho_identificador = TrabalhoSerializer()
    avaliadores = AvaliadorSerializer(many=True)

    class Meta:
        model = Avaliacao
        fields = '__all__'


class SessaoSerializer(serializers.ModelSerializer):

    departamento = DepartamentoSerializer()
    ano = AnoSerializer()
    sala = SalaSerializer()
    avaliacoes = AvaliacaoSerializer(many=True)

    class Meta:
        model = Sessao
        fields = fields = '__all__'
