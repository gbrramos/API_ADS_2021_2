from django import forms
from django.db.models import fields
from .models import Usuarios

class UsuariosForm(forms.ModelForm):

    class Meta:
        model =  Usuarios
        fields = ('nome', 'username', 'password', 'perfil')

        widgets = {
        'password': forms.PasswordInput(),
        }