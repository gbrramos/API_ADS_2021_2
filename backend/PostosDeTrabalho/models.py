from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.

class PostoDeTrabalho(models.Model):
    descricao = models.TextField()
    escala = models.CharField(max_length=255)
    numero_cadastro = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao
