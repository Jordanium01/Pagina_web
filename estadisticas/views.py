from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from catalogos.models import Clasificacion #aqui cambiar los datos de la tabla 
from estadisticas.serializers import claseSeria

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt #estas dos lineas tienen que estar pegadas a la funcion
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_Clasificacion(request):
	#Listar
	if request.method == 'GET':
		lista_api = Clasificacion.objects.all()
		serializer = claseSeria(lista_api, many = True)
		return Response(serializer.data)
		
	#Guardar
	elif request.method == 'POST':
		dataP = JSONParser().parse(request)
		serializer = claseSeria(data=dataP)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_clasificacion(request, id): #en id poner la llave primaria
	try:
		#esta variable es nueva
		varClass = Clasificacion.objects.get(idClasificacion = id)
	except Clasificacion.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
		
	if request.method == 'GET':
		serializer = claseSeria(varClass)
		return Response(serializer.data)	
	elif request.method == 'PUT':
		dataP = JSONParser().parse(request)
		serializer = claseSeria(varClass, data=dataP)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	elif request.method == "DELETE":
		varClass.delete() #delete a la BD
		return Response(status = status.HTTP_204_NO_CONTENT)