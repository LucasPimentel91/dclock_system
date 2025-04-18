from django.contrib import admin
from material.models import Material

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('mat_cod', 'mat_desc', 'mat_etq', 'mat_preco_unit', 'mat_fne', 'mat_dt_aqui', 'mat_obs')
    search_fields = ('mat_desc',)

admin.site.register(Material, MaterialAdmin)
