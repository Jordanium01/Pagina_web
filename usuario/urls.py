from django.urls import path
from.views import login, regis
urlpatterns = [
    path('login/', login, name="login"),
    path('register/', regis, name="register")
]

#path('login/', login, name="login"),
    #path('register/', regis, name="register"),

    #para que muestre la imagen
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)