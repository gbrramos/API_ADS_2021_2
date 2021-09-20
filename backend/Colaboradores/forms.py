from django import forms
from django.db.models import fields
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):

    class Meta:
        model =  Colaborador
        fields = ('cpf', 'matricula', 'nomeCompleto', 'dataAdmissao', 'dataDemissao', 'funcao', 'tipoDeCobertura', 'situacaoCadastro')

        widgets = {
            'dataAdmissao': forms.TextInput(attrs={'data-mask':"00/00/0000"}),
            'dataDemissao': forms.TextInput(attrs={'data-mask': "00/00/0000"}),
            'cpf': forms.TextInput(attrs={'data-mask': "000.000.000-00"})
            }