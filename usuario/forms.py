from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    #Contraseñas
    error_messages = {
        'password_mismatch': ("Las contraseñas no coinciden"),
        #'password_too_short': ("Contraseña muy corta"),
        #'password_too_common': ("Contrasenna muy comun"),
        #'password_entirely_numeric': ("Contraseña numerica")
    }
    username = forms.CharField(label='Nombre de usuario', error_messages={'unique': 'Ese usuario ya existe'})
    email = forms.EmailField(max_length=254, help_text='aiuda', label='Correo', error_messages={'invalid': 'Correo invalido'})
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repetir contraseña')
    #is_staff = forms.BooleanField( required=False, label='Es admin?')


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )