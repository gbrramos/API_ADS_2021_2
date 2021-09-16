from django.db import models
from django.db.models.fields import CharField, TextField


# Create your models here.
class Colaborador(models.Model):

    COBERTURA = (
        ('fixa', 'FIXA'),
        ('flutuante','FLUTUANTE'),
    )

    cpf = models.CharField(max_length=11)
    matricula = models.CharField(max_length=50)
    nomeCompleto = models.CharField(max_length=255)
    dataAdmissao = models.DateField()
    dataDemissao = models.DateField(null=True)
    funcao = TextField(max_length=255)
    tipoDeCobertura =  models.CharField(
        max_length=9,
        choices=COBERTURA,
    )
    situacaoCadastro = CharField(max_length=100) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nomeCompleto
