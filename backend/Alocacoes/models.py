from django.db import models
from django.db.models.fields import BooleanField
from Colaboradores.models import Colaborador
from PostosDeTrabalho.models import PostoDeTrabalho
# Create your models here.

class Alocacao(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, blank=True, null=True)
    posto = models.ForeignKey(PostoDeTrabalho, on_delete=models.CASCADE, blank=True, null=True)
    alocacao = models.BooleanField()