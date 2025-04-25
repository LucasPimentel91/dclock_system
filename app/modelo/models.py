from django.db import models

class Modelo(models.Model):
    mod_id = models.AutoField(primary_key=True)
    mod_nome = models.CharField(max_length=200, blank=True, null=True)

    
