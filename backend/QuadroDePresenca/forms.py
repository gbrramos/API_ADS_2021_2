from django import forms
from django.db.models import fields
from .models import QuadroDePresenca

class QuadroDePresencaForm(forms.ModelForm):

    class Meta:
        model =  QuadroDePresenca
        fields = ('data', 'colaborador', 'posto_trabalho')

        widgets = {
            'data': forms.TextInput(attrs={'data-mask':"00/00/0000"}),
        }
