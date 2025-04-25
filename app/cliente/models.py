from django.db import models

class Cliente(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_nome = models.CharField(max_length=255)
    cli_cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    cli_cnpj = models.CharField(max_length=18, unique=True, blank=True, null=True)
    cli_rg = models.CharField(max_length=20, blank=True, null=True)
    cli_dtnsc = models.DateField(blank=True, null=True)
    cli_end = models.CharField(max_length=255, blank=True, null=True)
    cli_end_num = models.CharField(max_length=10, blank=True, null=True)
    cli_end_cid = models.CharField(max_length=100, blank=True, null=True)
    cli_end_bairro = models.CharField(max_length=100, blank=True, null=True)
    cli_tel = models.CharField(max_length=20, blank=True, null=True)
    cli_cel = models.CharField(max_length=20, blank=True, null=True)
    cli_email = models.CharField(max_length=100, blank=True, null=True)
    cli_tipo = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.cli_nome