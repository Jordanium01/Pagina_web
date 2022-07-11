from django import forms
from django.forms import ModelForm
from .models import Juego, Clasificacion
from django.forms import ImageField
#Este proceso se repite por cada formulario

class proyectoFormulario(ModelForm):
	class Meta:
		model = Juego
		#Aqui van los campos que se rellenan (los incrementales no)
		fields = ['titulo','descripcion','caratula','annoSalida','precio','stock','genero','distribuidora']

class estadisticasFormulario(ModelForm):
	class Meta:
		model = Clasificacion
		#Aqui van los campos que se rellenan (los incrementales no)
		fields = ['pais','promedio','recaudado']

class registroestadisticas(ModelForm):
	class Meta:
		model = Clasificacion
		#Aqui van los campos que se rellenan (los incrementales no)
		fields = ['idClasificacion', 'pais','promedio','recaudado']