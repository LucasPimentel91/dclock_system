# Generated by Django 5.2 on 2025-04-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_id', models.AutoField(primary_key=True, serialize=False)),
                ('cli_nome', models.CharField(max_length=255)),
                ('cli_cpf', models.CharField(max_length=14, unique=True)),
                ('cli_cnpj', models.CharField(max_length=18, unique=True)),
                ('cli_rg', models.CharField(blank=True, max_length=20, null=True)),
                ('cli_dtnsc', models.DateField(blank=True, null=True)),
                ('cli_end', models.CharField(blank=True, max_length=255, null=True)),
                ('cli_end_num', models.CharField(blank=True, max_length=10, null=True)),
                ('cli_end_cid', models.CharField(blank=True, max_length=100, null=True)),
                ('cli_end_bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('cli_tel', models.CharField(blank=True, max_length=20, null=True)),
                ('cli_cel', models.CharField(blank=True, max_length=20, null=True)),
                ('cli_email', models.CharField(blank=True, max_length=100, null=True)),
                ('cli_tipo', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
