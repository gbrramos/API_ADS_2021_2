from django import forms
from django.db.models import fields
from .models import QuadroPresenca, Data


class QuadroDePresencaForm(forms.ModelForm):

    class Meta:
        model =  QuadroPresenca
        fields = ('data_id', 'presenca', 'colaboradores')

class DataForm(forms.ModelForm):

    class Meta:
        model = Data
        fields = ('dia', 'month', 'ano')
        