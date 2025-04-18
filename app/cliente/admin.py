from django.contrib import admin
from cliente.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cli_nome', 'cli_cpf', 'cli_rg', 'cli_end', 'cli_cel', 'cli_email', 'cli_tipo')
    search_fields = ('cli_nome',)

admin.site.register(Cliente, ClienteAdmin)
