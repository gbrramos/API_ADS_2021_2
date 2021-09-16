from django import forms
from django.db.models import fields
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):

    class Meta:
        model =  Colaborador
        fields = ('cpf', 'matricula', 'nomeCompleto', 'dataAdmissao', 'dataDemissao', 'funcao', 'tipoDeCobertura', 'situacaoCadastro')