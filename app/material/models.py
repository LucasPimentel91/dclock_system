from django.db import models

class Material(models.Model):
    mat_cod = models.AutoField(primary_key=True)
    mat_desc = models.CharField(max_length=255)
    mat_etq = models.IntegerField(blank=True, null=True)
    mat_preco_unit = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    mat_fne = models.CharField(max_length=200, blank=True, null=True)
    mat_dt_aqui = models.DateField(blank=True, null=True)
    mat_obs = models.TextField(blank=True, null=True)
