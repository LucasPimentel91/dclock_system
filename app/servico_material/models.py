from django.db import models
from servicos.models import Servico
from material.models import Material


class ServicoMaterial(models.Model):
    ser_id = models.ForeignKey(Servico, on_delete=models.PROTECT, related_name='servico')
    mat_cod = models.ForeignKey(Material, on_delete=models.PROTECT, related_name='material')
    quantidade = models.IntegerField()