from django.urls import path, include

from rest_framework import routers

from rest_framework.authtoken import views

from core.views import (DepartamentoViewSet, AnoViewSet, SalaViewSet,
                        AvaliadorViewSet, TrabalhoViewSet, TrabalhoAutorViewSet, SessaoViewSet,
                        AvaliacaoViewSet)

# DefaultRouter
router = routers.DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'anos', AnoViewSet)
router.register(r'salas', SalaViewSet)
router.register(r'avaliadores', AvaliadorViewSet)
router.register(r'trabalhos', TrabalhoViewSet)
router.register(r'trabalho_autores', TrabalhoAutorViewSet)
router.register(r'sessoes', SessaoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

# URLs
urlpatterns = []

urlpatterns += router.urls
