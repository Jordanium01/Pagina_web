from django.db import models
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
    widget = models.CharField(max_length=100, verbose_name='Iframe:')#widget de steam que actualiza los precios
    genero = models.ForeignKey(GeneroJuego, on_delete=models.CASCADE) #union a "GeneroJuego"
    distribuidora = models.ForeignKey(DistribuidoraJuego, on_delete=models.CASCADE) #union a "Distribuidora" 

    def __str__(self):
        return str(self.titulo)
    
class Clasificacion(models.Model):
    #idClasificacion = models.AutoField(primary_key=True, verbose_name='Id')
    #idClasificacion = models.ForeignKey(Juego, on_delete=models.CASCADE, primary_key=True, verbose_name='Id')
    idClasificacion = models.OneToOneField(Juego,  on_delete=models.CASCADE , primary_key=True ,unique=True, verbose_name='id')
    #juego = models.ForeignKey(Juego, on_delete=models.CASCADE) #union a "Juego"
    pais = models.CharField(max_length=50, verbose_name='Pais')
    promedio = models.IntegerField(verbose_name='Promedio jugadores:')
    fecha = models.DateField(verbose_name='Updates:')
    recaudado = models.IntegerField(verbose_name='Dinero recaudado:')
    

    def __str__(self):
        return str(self.idClasificacion)