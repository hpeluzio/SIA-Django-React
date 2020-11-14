from django.contrib.auth.models import User, Group
from rest_framework import serializers

from core.models import (Departamento, Ano, Sala,
                         Avaliador, Trabalho, TrabalhoAutor,
                         Sessao, Avaliacao, AvaliadorAvaliacao)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


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
    class Meta:
        model = Avaliador
        fields = '__all__'


class TrabalhoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trabalho
        fields = '__all__'


class TrabalhoAutorSerializer(serializers.ModelSerializer):

    trabalho_id = TrabalhoSerializer()

    class Meta:
        model = TrabalhoAutor
        fields = '__all__'


class SessaoSerializer(serializers.ModelSerializer):

    departamento_id = DepartamentoSerializer()
    ano_id = AnoSerializer()
    sala_id = SalaSerializer()

    class Meta:
        model = Sessao
        fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):

    sessao_id = SessaoSerializer()
    trabalho_id = TrabalhoSerializer()

    class Meta:
        model = Avaliacao
        fields = '__all__'


class AvaliadorAvaliacaoSerializer(serializers.ModelSerializer):

    avaliador_id = AvaliadorSerializer()
    avaliacao_id = AvaliacaoSerializer()

    class Meta:
        model = AvaliadorAvaliacao
        fields = '__all__'
