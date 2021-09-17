from django import forms
from django.db.models import fields
from .models import Clientes

class ClientesForm(forms.ModelForm):

    class Meta:
        model =  Clientes
        fields = ('nome_fantasia', 'razao_social', 'cnpj', 'contato', 'funcao')