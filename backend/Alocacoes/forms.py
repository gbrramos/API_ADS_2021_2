from django import forms
from django.forms import widgets
from django import forms
from django.db.models import fields
from .models import Alocacao


class AlocacoesForms(forms.ModelForm):

    class Meta:
        model =  Alocacao
        fields = ('colaborador', 'posto', 'alocacao',)