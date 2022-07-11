from dataclasses import field
from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Para la informacion extra del usuario
from django.forms import ModelForm
from usuario.models import UserExtraInfo


class SignUpForm(UserCreationForm):
    #Contraseñas
    error_messages = {
        'password_mismatch': ("Las contraseñas no coinciden"),
    }
    username = forms.CharField(label='Nombre de usuario', error_messages={'unique': 'Ese usuario ya existe'})
    email = forms.EmailField(max_length=254, label='Correo', error_messages={'invalid': 'Correo invalido'})
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repetir contraseña')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

class ExtraInformation(ModelForm):
    id = 0
    is_suscribe = forms.BooleanField( required=False, label='¿Quieres suscribirte?')
    direccion = forms.CharField( required=True, label='Direccion')
    
    class Meta:
        model = UserExtraInfo
        fields = ('id','is_suscribe','direccion')