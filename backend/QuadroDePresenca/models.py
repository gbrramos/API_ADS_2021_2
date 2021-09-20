from django.db import models
from django.db.models.fields import CharField, TextField


# Create your models here.
class QuadroDePresenca(models.Model):

    data = models.CharField(max_length=255)
    colaborador = models.CharField(max_length=50)
    posto_trabalho = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.data
