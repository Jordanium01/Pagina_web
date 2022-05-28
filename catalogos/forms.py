from django import forms
from django.forms import ModelForm
from .models import Juego

#Este proceso se repite por cada formulario
class proyectoFormulario(ModelForm):
	class Meta:
		model = Juego
		#Aqui van los campos que se rellenan (los incrementales no)
		fields = ['titulo','descripcion','caratula','annoSalida','widget','genero','distribuidora']