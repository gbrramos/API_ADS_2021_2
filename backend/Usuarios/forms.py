from django import forms
from django.db.models import fields
from django.contrib.auth.models import User

class UsuariosForm(forms.ModelForm):

    class Meta:
        model =  User
        fields = ('username', 'password',  'email', 'is_superuser')

        widgets = {
        'password': forms.PasswordInput(),
        }