from django.contrib import admin
from funcionario.models import Funcionario

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('func_nome', 'func_tel', 'func_cel', 'func_email', 'func_cargo')
    search_fields = ('func_nome',)

admin.site.register(Funcionario, FuncionarioAdmin)
