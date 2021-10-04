from django import forms
from django.db.models import fields
from .models import QuadroPresenca, Data


class QuadroDePresencaForm(forms.ModelForm):

    class Meta:
        model =  QuadroPresenca
        fields = ('data', 'presenca', 'colaboradores')

        widgets = {
            'data': forms.TextInput(attrs={'data-mask':"00/00/0000"}),
        }

class DataForm(forms.ModelForm):

    class Meta:
        model = Data
        fields = ('data',)
        widgets = {
            'data': forms.TextInput(attrs={'data-mask':"00/00/0000"}),
        }