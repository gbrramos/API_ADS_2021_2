from django.db import models

# Create your models here.
class Colaboradores(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    data_admissao = models.CharField(max_length=255)
    data_demissao = models.CharField(max_length=255)
    situacao_cadastro = models.CharField(max_length=255)
    funcao = models.CharField(max_length=255)
    tipo_cobertura = models.CharField(max_length=255)