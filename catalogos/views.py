from django.shortcuts import render, redirect
from .models import Juego, Clasificacion
from .forms import proyectoFormulario, estadisticasFormulario, registroestadisticas
import datetime

#crear clase para el objeto
'''class Persona:
	#constructor de una clase en python
	def __init__(self,rut,nombre,edad):
		self.rut=rut
		self.nombre=nombre
		self.edad=edad
		super().__init__()#aqui llama al constructor del padre'''
		

# Create your views here.
def home(request):
		return render(request,'catalogos/index.html')

def faq(request):
		return render(request,'catalogos/FAQ.html')

def contacts(request):
		return render(request,'catalogos/contacto.html')

def login(request):
		return render(request,'usuario/login.html')

def regis(request):
		return render(request,'usuario/registro.html')

def proyects(request):
		#esto hace un SELECT * FROM nombreTabla, y lo ingresa a la variable 
		ListaJuegos = Juego.objects.all()
		ListaEstadisticas = Clasificacion.objects.all()

		#aqui se ponen todos los datos a rescatar
		juegos = {
			'registroJuegos': ListaJuegos,
			'validacionEst': ListaEstadisticas

		}
		return render(request,'catalogos/proyectos.html',juegos)

def estadisticas(request):
		clasificaciones = Clasificacion.objects.all()
		datos = {
			'form_estadistica':clasificaciones
		}
		return render(request,'catalogos/proyectos_estadistica.html', datos)

def estadistica_individual(request,id):
		clasificacion = Clasificacion.objects.filter(idClasificacion_id=id)
		datos = {
			'registroEstadistica':clasificacion
		}
		return render(request,'catalogos/estadistica_individual.html', datos)

def form_statis(request):
	#Mostrar el formulario del form al html
	datos = {
		'estadisticas_formulario':registroestadisticas()
	}
	#guardar los datos del formulario
	if (request.method == 'POST'):
		#rescatar la informacion
		varFormulario = registroestadisticas(request.POST,request.FILES)# + fecha
		if varFormulario.is_valid():
			varFormulario.save() #insert a la base de datos
			datos['mensaje'] = 'Estadistica ingresada'#mensaje de existo
		else:
			#mensaje de error
			datos['mensaje'] = 'Error al guardar'
	return render(request,'catalogos/registro_estadistica.html',datos)

def mod_statis(request, id):
	ListaEstadistica = Clasificacion.objects.get(idClasificacion_id=id)#Select * from tabla where idjuego=id

	#aqui se ponen todos los datos a rescatar
	datos = {
		'mod_estadistica': estadisticasFormulario(instance=ListaEstadistica)
	}

	if (request.method == 'POST'):
		formulario = estadisticasFormulario(request.POST,request.FILES, instance=ListaEstadistica)
		if formulario.is_valid():
			formulario.save()
			#actualizar la fecha de actualizacion de la tabla
			Clasificacion.objects.filter(idClasificacion_id=id).update(fecha = datetime.datetime.now().date() )

			datos['mensaje'] = 'Estadistica modificada'#mensaje de existo
			return redirect(to='estadisticas')
		else:
			datos['mensaje'] = 'Error al modificar'#mensaje de existo
	return render(request,'catalogos/modificacion_estadistica.html',datos)

def del_statis(request, id):
	ListaEstadistica = Clasificacion.objects.get(idClasificacion_id=id)#Select * from tabla where idjuego=id
	ListaEstadistica.delete()

	return redirect(to='estadisticas')

def form_proyects(request):
	#Mostrar el formulario del form al html
	datos = {
		'proyecto_formulario':proyectoFormulario()
	}
	#guardar los datos del formulario
	if (request.method == 'POST'):
		#rescatar la informacion
		varFormulario = proyectoFormulario(request.POST,request.FILES)
		if varFormulario.is_valid():
			varFormulario.save() #insert a la base de datos
			datos['mensaje'] = 'Juego ingresado'#mensaje de existo
		else:
			#mensaje de error
			datos['mensaje'] = 'Error al guardar'
	return render(request,'catalogos/registro_proyecto.html',datos)

def mod_proyects(request, id):
	ListaJuegos = Juego.objects.get(idjuego=id)#Select * from tabla where idjuego=id

	#aqui se ponen todos los datos a rescatar
	datos = {
		'mod_formulario': proyectoFormulario(instance=ListaJuegos)
	}

	if (request.method == 'POST'):
		formulario = proyectoFormulario(request.POST,request.FILES, instance=ListaJuegos)
		if formulario.is_valid():
			formulario.save()
			datos['mensaje'] = 'Juego modificado'#mensaje de existo
			return redirect(to='proyectos')
		else:
			datos['mensaje'] = 'Error al modificar'#mensaje de existo
	return render(request,'catalogos/modificacion_proyecto.html',datos)
	#return redirect(to='proyectos')

def del_proyects(request, id):
	ListaJuegos = Juego.objects.get(idjuego=id)#Select * from tabla where idjuego=id
	ListaJuegos.delete()

	return redirect(to='proyectos')

def qsomos(request):
		return render(request,'catalogos/quienesSomos.html')