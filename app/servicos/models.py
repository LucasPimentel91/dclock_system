from django.db import models
from cliente.models import Cliente
from funcionario.models import Funcionario

class Servico(models.Model):
    ser_id = models.AutoField(primary_key=True)
    ser_cli_id = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='servico_cliente')
    ser_usr_id = models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name='servico_funcionario')
    ser_desc = models.TextField(blank=True, null=True)
    ser_tipo_servico = models.CharField(max_length=1, blank=True, null=True)
    ser_preco_total = models.DecimalField(max_digits=5, decimal_places=2)

    
