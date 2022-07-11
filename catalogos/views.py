from django.shortcuts import render, redirect
from .models import Juego, Clasificacion, Compras
import random
from .Carrito import Carrito
from .forms import proyectoFormulario, estadisticasFormulario, registroestadisticas
from datetime import datetime, timedelta
import datetime


#Informacion extra del usuario
from usuario.models import UserExtraInfo

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
		nombreJuego = Juego.objects.all()
		datos = {
			'form_estadistica':clasificaciones,
			'juegos':nombreJuego
		}
		return render(request,'catalogos/proyectos_estadistica.html', datos)

def estadistica_individual(request,id):
		clasificacion = Clasificacion.objects.filter(idClasificacion_id=id)
		nombreJuego = Juego.objects.all()
		datos = {
			'registroEstadistica':clasificacion,
			'juegos':nombreJuego
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

def tienda(request):
	productos = Juego.objects.all()

	#No me dejo comparar los username, asi que compare las id
	try:
		InformacionUsuario = UserExtraInfo.objects.get(id_id=request.user.id)
	except UserExtraInfo.DoesNotExist:
		InformacionUsuario = None
		
	print(InformacionUsuario)
	#aqui se ponen todos los datos a rescatar
	datos = {
		'ext_usuario': InformacionUsuario,
		'productos':productos
	}
	return render(request, 'catalogos/Tienda.html', datos)

def agregar_producto(request, producto_id):
	carrito = Carrito(request)
	producto = Juego.objects.get(idjuego=producto_id)
	carrito.agregar(producto)
	return redirect("Tienda")

def eliminar_producto(request, producto_id):
	carrito = Carrito(request)
	producto = Juego.objects.get(idjuego=producto_id)
	carrito.eliminar(producto)
	return redirect("Tienda")

def restar_producto(request, producto_id):
	carrito = Carrito(request)
	producto = Juego.objects.get(idjuego=producto_id)
	carrito.restar(producto)
	return redirect("Tienda")

def limpiar_carrito(request):
	carrito = Carrito(request)
	carrito.limpiar()
	return redirect("Tienda")

def restar_stock(cantidad,juegoid):
	proyecto = Juego.objects.get(idjuego=juegoid)
	proyecto.stock -= cantidad
	proyecto.save()

def comprar(request):
	producto = ''
	precio_total = 0

	if "carrito" in request.session.keys():
		for key, value in request.session["carrito"].items():
			restar_stock(int(value["cantidad"]),int(value["producto_id"]))
			producto = producto + value["nombre"] + ', '
			precio_total = precio_total + value["acumulado"]
			
	try:
		InformacionUsuario = UserExtraInfo.objects.get(id_id=request.user.id)

		if InformacionUsuario.is_suscribe:
			precio_total = round(precio_total*0.95)
	except UserExtraInfo.DoesNotExist:
		InformacionUsuario = None

	

	cliente = request.user.username
	numeroCompra = random.randint(10000,99999)
	dias_estimacion = random.randint(4,7)

	while Compras.objects.filter(idcompra=numeroCompra).exists():
		numeroCompra+=1
	else:
		Compras.objects.create(idcompra=numeroCompra,comprador=str(cliente),estado=0,total=precio_total,articulos=producto,fechaCompra=datetime.datetime.now(),estimacionllegada=datetime.date.today() + timedelta(days=dias_estimacion))

	limpiar_carrito(request)	
	return redirect("Tienda")

def historial_compras(request):
	#Mostrar el formulario del form al html
	if request.user.is_authenticated and request.user.is_staff == 1:
		ListaCompras = Compras.objects.all().order_by('-fechaCompra')
		datos = {
			'historialCompras':ListaCompras
		}
	else:
		ListaCompras = Compras.objects.filter(comprador=request.user.username).order_by('-fechaCompra')
		datos = {
			'historialCompras':ListaCompras
		}
	return render(request,'catalogos/historial_compras.html',datos)

def detalle_compra(request,id):
		compra = Compras.objects.filter(idcompra=id)
		datos = {
			'compradetalle':compra
		}
		return render(request,'catalogos/detalle_compras.html', datos)


def aumentar_estado(self, compra_id):
	compra = Compras.objects.get(idcompra=compra_id)
	compra.estado += 1
	#Si despues de aumentar, la compra queda como "despachada", crear fecha de llegada
	if compra.estado == 2:
		compra.fechallegada=datetime.datetime.now()
	compra.save()
	return redirect("http://127.0.0.1:8000/detalle-compra/"+str(compra_id))

def disminuir_estado(self, compra_id):
	compra = Compras.objects.get(idcompra=compra_id)
	compra.estado -= 1
	compra.save()
	return redirect("http://127.0.0.1:8000/detalle-compra/"+str(compra_id))