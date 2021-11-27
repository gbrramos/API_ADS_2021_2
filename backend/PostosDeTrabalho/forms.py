from django import forms
from django.db.models import fields
from .models import PostoDeTrabalho

class PostosDeTrabalhoForms(forms.ModelForm):

    class Meta:
        model =  PostoDeTrabalho
        fields = ('descricao', 'escala', 'limites_multa', 'numero_cadastro')