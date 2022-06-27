from django.contrib import admin
from .models import GeneroJuego, Juego, DistribuidoraJuego, Clasificacion

# Register your models here.
admin.site.register(GeneroJuego)
admin.site.register(Juego)
admin.site.register(DistribuidoraJuego)

# Register your models here.
admin.site.register(Clasificacion)