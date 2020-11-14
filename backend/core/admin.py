from django.contrib import admin

from core.models import Ano, Departamento


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Departamento._meta.fields]
    # list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Ano)
class AnoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Ano._meta.fields]
    # list_display = ('cargo', 'ativo', 'modificado')
