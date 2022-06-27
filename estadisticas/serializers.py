from rest_framework import serializers
#Aqui especifico de donde viene el model
from catalogos.models import Clasificacion

class claseSeria(serializers.ModelSerializer):
	#aqui igual que en el forms de la aplicacion anterior
	class Meta:
		model = Clasificacion
		fields = ['idClasificacion','pais','promedio','fecha','recaudado']