from django.db import models
from django.db.models.fields import CharField, TextField


# Create your models here.
class Clientes(models.Model):

    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)
    endereco = CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_fantasia
