from django.urls import path
from estadisticas.views import lista_Clasificacion, detalle_clasificacion

urlpatterns = [
	path('lista_Clasificacion', lista_Clasificacion, name="lista_Clasificacion"),
    path('detalle_clasificacion/<id>',detalle_clasificacion,name="detalle_clasificacion"),
]
