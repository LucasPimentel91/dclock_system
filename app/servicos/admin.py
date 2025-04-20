from django.contrib import admin
from servicos.models import Servico
#from servico_material.models import ServicoMaterial

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('ser_desc', 'ser_tipo_servico', 'ser_cli_id', 'ser_usr_id', 'ser_preco_total')
    search_fields = ('ser_cli_id', 'ser_tipo_servico',)

admin.site.register(Servico, ServicoAdmin)
#admin.site.register(ServicoMaterial, ServicoAdmin)