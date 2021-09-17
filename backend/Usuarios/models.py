from django.db import models
from django.db.models.fields import CharField, TextField

class Usuarios(models.Model):

    STATUS  = (
        ('tatico','TÁTICO'),
        ('operacional','OPERACIONAL'),
    )

    nome = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    perfil = models.CharField(max_length=11, choices=STATUS)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
