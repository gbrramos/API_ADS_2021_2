from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.json import ContainedBy
from Colaboradores.models import Colaborador
from PostosDeTrabalho.models import PostoDeTrabalho


# Create your models here.
class QuadroDePresenca(models.Model):

    data = models.TextField(max_length=10)
    presenca = models.BooleanField(default=False)

    def __str__(self):
        return self.data
