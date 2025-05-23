# Generated by Django 5.2 on 2025-04-20 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('ser_id', models.AutoField(primary_key=True, serialize=False)),
                ('ser_desc', models.TextField(blank=True, null=True)),
                ('ser_tipo_servico', models.CharField(blank=True, max_length=1, null=True)),
                ('ser_preco_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ser_cli_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='servico_cliente', to='cliente.cliente')),
                ('ser_usr_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='servico_funcionario', to='funcionario.funcionario')),
            ],
        ),
    ]
