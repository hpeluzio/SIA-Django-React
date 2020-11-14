from django.urls import path, include

from rest_framework import routers

from core.views import UserViewSet, GroupViewSet
from core.views import DepartamentoViewSet, AnoViewSet

# DefaultRouter
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'anos', AnoViewSet)

# URLs
urlpatterns = [
    # path('cursos/', CursoAPIView.as_view()),
    # path('alunos/', AlunoAPIView.as_view()),
    # path('alunosfbv/', alunofbv),
    # path('alunofbv_insert/', alunofbv_insert),

]

urlpatterns += router.urls
