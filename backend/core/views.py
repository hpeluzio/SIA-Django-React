from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from core.models import (Departamento, Ano, Sala,
                         Avaliador, Trabalho, TrabalhoAutor,
                         Sessao, Avaliacao)
from core.serializers import (DepartamentoSerializer, AnoSerializer, SalaSerializer,
                              AvaliadorSerializer, TrabalhoSerializer, TrabalhoAutorSerializer, SessaoSerializer,
                              AvaliacaoSerializer)


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class AnoViewSet(viewsets.ModelViewSet):
    queryset = Ano.objects.all()
    serializer_class = AnoSerializer


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class AvaliadorViewSet(viewsets.ModelViewSet):
    queryset = Avaliador.objects.all()
    serializer_class = AvaliadorSerializer


class TrabalhoViewSet(viewsets.ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer


class TrabalhoAutorViewSet(viewsets.ModelViewSet):
    queryset = TrabalhoAutor.objects.all()
    serializer_class = TrabalhoAutorSerializer


class SessaoViewSet(viewsets.ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
