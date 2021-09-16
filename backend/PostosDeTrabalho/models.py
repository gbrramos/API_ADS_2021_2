from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.

class PostoDeTrabalho(models.Model):
    descricao = models.TextField()
    escala = models.CharField(max_length=255)

