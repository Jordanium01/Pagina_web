from django.shortcuts import render, redirect
from .models import Juego
from .forms import proyectoFormulario

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

		#aqui se ponen todos los datos a rescatar
		juegos = {
			'registroJuegos': ListaJuegos
		}
		return render(request,'catalogos/proyectos.html',juegos)

#def form_proyects(request):
	#return render(request,'catalogos/registro_proyecto.html')
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
		formulario = proyectoFormulario(request.POST, request.FILES, instance=ListaJuegos)
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