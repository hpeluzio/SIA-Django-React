from django.contrib import admin

from core.models import (Departamento, Ano, Sala,
                         Avaliador, Trabalho, TrabalhoAutor, Sessao,
                         Avaliacao)


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Departamento._meta.fields]


@admin.register(Ano)
class AnoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Ano._meta.fields]


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Sala._meta.fields]


@admin.register(Avaliador)
class AvaliadorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Avaliador._meta.fields]


@admin.register(Trabalho)
class TrabalhoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Trabalho._meta.fields]


@admin.register(TrabalhoAutor)
class TrabalhoAutorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrabalhoAutor._meta.fields]
    # list_display = ('trabalho_id', 'autor')


@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Sessao._meta.fields]


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Avaliacao._meta.fields]
