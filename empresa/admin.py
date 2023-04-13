from django.contrib import admin
from .models import Departamento, Funcionario, Projeto, ProjetoFuncionario

class FuncionarioInline(admin.TabularInline):
    model = ProjetoFuncionario
    extra = 1

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'horas_necessarias', 'prazo_estimado', 'horas_realizadas', 'ultimo_calculo_horas', 'departamento', 'supervisor')
    search_fields = ('nome', 'departamento__nome')
    list_filter = ('departamento', 'supervisor')

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'rg', 'sexo', 'data_nascimento', 'habilitacao', 'salario', 'carga_horaria_semanal', 'departamento')
    search_fields = ('nome', 'cpf', 'rg', 'departamento__nome')
    list_filter = ('sexo', 'habilitacao', 'departamento')
    inlines = [FuncionarioInline]

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Projeto, ProjetoAdmin)
