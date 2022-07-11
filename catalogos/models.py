from pyexpat import model
from django.db import models
import datetime

#Genero juego
class GeneroJuego(models.Model): #tablas
    idGenero = models.IntegerField(primary_key=True,verbose_name='Id') #columnas
    nombreGenero = models.CharField(max_length=50,verbose_name='Genero')

    #metodo que devuelve un objeto de la clase (como string) 
    def __str__(self):
        return self.nombreGenero #esta es la cadena de caracteres se devolvera, la puedo modificar con + "" + para agregar mas cosas con espacios

class DistribuidoraJuego(models.Model): #tablas
    idDistribuidora = models.IntegerField(primary_key=True,verbose_name='Id') #columnas
    nombreDistribuidora = models.CharField(max_length=30,verbose_name='Nombre')
    logoDistribuidora =  models.ImageField(upload_to='catalogos/static/catalogos/img', verbose_name='Logo')
    fundacionDistribuidora = models.CharField(max_length=30,verbose_name='Fundacion')

    def __str__(self):
        return self.nombreDistribuidora #esta es la cadena de caracteres se devolvera, la puedo modificar con + "" + para agregar mas cosas con espacios

class Juego(models.Model):
    idjuego = models.AutoField(primary_key=True, verbose_name='Id')
    titulo = models.CharField(max_length=50, verbose_name='Titulo:') #nombre
    descripcion = models.TextField(max_length=500, verbose_name='Descripcion:')
    caratula = models.ImageField(upload_to='catalogos/static/catalogos/img', verbose_name='Caratula:')
    annoSalida = models.IntegerField(verbose_name='Año salida:') #anno salida
    widget = models.CharField(max_length=100, default='' ,verbose_name='Iframe:')#widget de steam que actualiza los precios
    genero = models.ForeignKey(GeneroJuego, on_delete=models.CASCADE) #union a "GeneroJuego"
    distribuidora = models.ForeignKey(DistribuidoraJuego, on_delete=models.CASCADE) #union a "Distribuidora" 
    precio = models.IntegerField(verbose_name='precio:')
    stock = models.IntegerField(verbose_name='Stock:')

    def __str__(self):
        #return f'{self.titulo} -> {self.precio}'
        return self.titulo

class Compras(models.Model):
    idcompra = models.IntegerField(primary_key=True, verbose_name='id:')
    comprador = models.CharField(max_length=100, verbose_name='Comprador:') #nombre del comprador
    estado = models.IntegerField(verbose_name='Estado de la compra:')
    total = models.IntegerField(verbose_name='Precio de la compra:')
    articulos = models.CharField(max_length=100, verbose_name='compras:') #nombre del comprador
    fechaCompra = models.DateTimeField(verbose_name='fecha de compra:', null=True)
    estimacionllegada = models.DateTimeField(verbose_name='fecha de estimacion de llegada:', null=True)
    fechallegada = models.DateTimeField(verbose_name='fecha de llegada:', null=True)

    def __str__(self):
        return str(self.idcompra)
    
class Paises(models.Model):
    idPais = models.AutoField(primary_key=True, verbose_name='Id')
    pais = models.CharField(max_length=50, verbose_name='Pais')

    def __str__(self):
        return str(self.pais)

class Clasificacion(models.Model):
    idClasificacion = models.OneToOneField(Juego,  on_delete=models.CASCADE , primary_key=True ,unique=True, verbose_name='id')
    #pais = models.CharField(max_length=50, verbose_name='Pais')
    pais = models.OneToOneField(Paises,  on_delete=models.CASCADE ,unique=True, verbose_name='Pais:')
    promedio = models.IntegerField(verbose_name='Promedio jugadores:')
    fecha = models.DateField(auto_now_add=True, verbose_name='Fecha de actualizacion:')
    recaudado = models.IntegerField(verbose_name='Dinero recaudado:')
    
    def __str__(self):
        return str(self.idClasificacion)


#No se ocupa, me da miedo borrarlo
class Usuario(models.Model):
    correo = models.CharField(max_length=50, primary_key=True, verbose_name='Correo')
    pnombre = models.CharField(max_length=100, verbose_name='PNombre')
    snombre = models.CharField(max_length=100, verbose_name='SNombre')
    apaterno = models.CharField(max_length=100, verbose_name='APaterno')
    amaterno = models.CharField(max_length=100, verbose_name='AMaterno')
    pais = models.CharField(max_length=50, verbose_name='Pais')
    clave = models.CharField(max_length=16, verbose_name='clave')

    def __str__(self):
        return str(self.correo)