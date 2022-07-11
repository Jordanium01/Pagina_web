from django.db import models
from django.contrib.auth.models import User
from pkg_resources import require

# Create your models here.
class UserExtraInfo(models.Model): #tablas
    id = models.OneToOneField(User,  on_delete=models.CASCADE , primary_key=True ,unique=True, verbose_name='id')
    is_suscribe = models.BooleanField(verbose_name="suscrito: ")
    direccion = models.CharField(max_length=300, verbose_name="Direccion: ", default='')

    #metodo que devuelve un objeto de la clase (como string) 
    def __str__(self):
        return str(self.id) #esta es la cadena de caracteres se devolvera, la puedo modificar con + "" + para agregar mas cosas con espacios