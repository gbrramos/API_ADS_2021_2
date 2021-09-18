from django.db import models
from django.db.models.fields import CharField, TextField
from Clientes.models import Clientes
from PostosDeTrabalho.models import PostoDeTrabalho

# Create your models here.

class Contrato(models.Model):
    numero = models.IntegerField()
    valor = models.FloatField()
    cliente = models.ForeignKey(
        Clientes,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="cliente_id",  
    )
    postoDeTrabalho = models.ManyToManyField(PostoDeTrabalho)






