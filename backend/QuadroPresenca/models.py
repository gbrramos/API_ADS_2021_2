from django.db import models
from django.db.models.fields import CharField, TextField, DateField
from django.db.models.fields.json import ContainedBy
from Colaboradores.models import Colaborador
from PostosDeTrabalho.models import PostoDeTrabalho

# Create your models here.

class Data(models.Model):

    data = models.DateField(blank=True, null=True)

class QuadroPresenca(models.Model):

    presenca = models.BooleanField(default=False)
    colaboradores = models.ForeignKey(Colaborador, on_delete=models.CASCADE, blank=True, null=True)
    data = models.OneToOneField(Data, on_delete=models.CASCADE)


    def __str__(self):
        return self.data
