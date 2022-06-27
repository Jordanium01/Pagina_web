from django.contrib import admin
from .models import GeneroJuego, Juego, DistribuidoraJuego, Clasificacion, Usuario, Paises

# Register your models here.
admin.site.register(GeneroJuego)
admin.site.register(Juego)
admin.site.register(DistribuidoraJuego)
admin.site.register(Clasificacion)
admin.site.register(Usuario)
admin.site.register(Paises)