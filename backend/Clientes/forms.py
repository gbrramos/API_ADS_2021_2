from django import forms
from django.db.models import fields
from .models import Clientes

class ClientesForm(forms.ModelForm):

    class Meta:
        model =  Clientes
        fields = ('nome_fantasia', 'razao_social', 'cnpj', 'contato', 'funcao')

        widgets = {
            'contato': forms.TextInput(attrs={'data-mask':"(00) 00000-0000"}),
            'cnpj': forms.TextInput(attrs={'data-mask': "00.000.000/0000-00"})
            }