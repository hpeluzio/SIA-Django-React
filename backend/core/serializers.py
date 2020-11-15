from django.contrib.auth.models import User, Group
from rest_framework import serializers

from core.models import (Departamento, Ano, Sala,
                         Avaliador, Trabalho, TrabalhoAutor,
                         Sessao, Avaliacao)


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

    # print([f.name for f in Trabalho._meta.fields])

    # print(lista)

    class Meta:
        list_fields = [f.name for f in Trabalho._meta.fields]
        list_fields.append('autores')
        model = Trabalho
        # fields = Trabalho.__dict__
        fields = list_fields
        depth = 1


class TrabalhoAutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrabalhoAutor
        fields = '__all__'
        depth = 1


class SessaoSerializer(serializers.ModelSerializer):

    class Meta:
        list_fields = [f.name for f in Sessao._meta.fields]
        list_fields.append('avaliacoes')
        model = Sessao
        fields = list_fields
        depth = 2


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = '__all__'
        depth = 2
