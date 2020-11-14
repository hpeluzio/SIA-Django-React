from django.urls import path, include

from rest_framework import routers

from core.views import UserViewSet, GroupViewSet
from core.views import (DepartamentoViewSet, AnoViewSet, SalaViewSet,
                        AvaliadorViewSet, TrabalhoViewSet, TrabalhoAutorViewSet)

# DefaultRouter
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'anos', AnoViewSet)
router.register(r'salas', SalaViewSet)
router.register(r'avaliadores', AvaliadorViewSet)
router.register(r'trabalhos', TrabalhoViewSet)
router.register(r'trabalho_autores', TrabalhoAutorViewSet)

# URLs
urlpatterns = [
    # path('cursos/', CursoAPIView.as_view()),
    # path('alunos/', AlunoAPIView.as_view()),
    # path('alunosfbv/', alunofbv),
    # path('alunofbv_insert/', alunofbv_insert),

]

urlpatterns += router.urls
