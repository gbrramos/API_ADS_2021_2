from django.forms import widgets
from PostosDeTrabalho.models import PostoDeTrabalho
from django import forms
from django.db.models import fields
from .models import Contrato
from PostosDeTrabalho.models import PostoDeTrabalho


class CustomPostoDeTrabalho(forms.ModelMultipleChoiceField):
    def label_from_instance(self, postoDeTrabalho):
        return "%s" % postoDeTrabalho.descricao
class ContratosForms(forms.ModelForm):

    class Meta:
        model =  Contrato
        fields = ['numero', 'valor','cliente', 'postoDeTrabalho']

    postoDeTrabalho = CustomPostoDeTrabalho(
        queryset=PostoDeTrabalho.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
