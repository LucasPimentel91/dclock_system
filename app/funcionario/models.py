from django.db import models

class Funcionario(models.Model):
    func_id = models.AutoField(primary_key=True)
    func_nome = models.CharField(max_length=255)
    func_cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    func_rg = models.CharField(max_length=20, blank=True, null=True)
    func_tel = models.CharField(max_length=20, blank=True, null=True)
    func_cel = models.CharField(max_length=20, blank=True, null=True)
    func_email = models.CharField(max_length=100, blank=True, null=True)
    func_cargo = models.CharField(max_length=200, blank=True, null=True)
