from django.contrib.auth.models import User, Group
from rest_framework import serializers

from core.models import Departamento, Ano


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class AnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ano
        fields = '__all__'
