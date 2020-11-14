from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import UserSerializer, GroupSerializer

from core.models import (Departamento, Ano, Sala,
                         Avaliador, Trabalho, TrabalhoAutor)
from core.serializers import (DepartamentoSerializer, AnoSerializer, SalaSerializer,
                              AvaliadorSerializer, TrabalhoSerializer, TrabalhoAutorSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


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
