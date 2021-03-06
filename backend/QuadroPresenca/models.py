from django.db import models
from django.db.models.fields import CharField, TextField, DateField
from django.db.models.fields.json import ContainedBy
from Colaboradores.models import Colaborador
from PostosDeTrabalho.models import PostoDeTrabalho

# Create your models here.

class Data(models.Model):

    dia = models.TextField(blank=True, null=True)
    month = models.TextField(blank=True, null=True)
    ano = models.TextField(blank=True, null=True)

    def __date__(self):
        return self.dia

class QuadroPresenca(models.Model):

    presenca = models.BooleanField(default=False)
    colaboradores = models.ForeignKey(Colaborador, on_delete=models.CASCADE, blank=True, null=True)
    data_id = models.ManyToManyField(Data)
    justificativa = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __int__(self):
        return self.colaboradores


class Dashboard(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    quant_presenca = models.IntegerField()

    def __int__(self):
        return self.quant_presenca