from django.contrib import admin
from .models import GeneroJuego, Juego, DistribuidoraJuego, Clasificacion, Paises, Compras
from usuario.models import UserExtraInfo

# Register your models here.
admin.site.register(GeneroJuego)
admin.site.register(Juego)
admin.site.register(DistribuidoraJuego)
admin.site.register(Clasificacion)
admin.site.register(Paises)
admin.site.register(Compras)

admin.site.register(UserExtraInfo)