from django.urls import path
from.views import home, faq, contacts, proyects, qsomos, login, regis, form_proyects, mod_proyects, del_proyects
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', funcion, alias)
    path('', home,name="index"),
    path('contacto/', contacts, name="contacto"),
    path('faq/', faq, name="faq"),
    path('login/', login, name="login"),
    path('register/', regis, name="register"),
    path('proyectos/', proyects, name="proyectos"),
    #path('formulario_proyectos/', form_proyects, name="fom_proyectos"),
    path('formulario_proyectos/',form_proyects,name="fom_proyectos"),
    path('modificar_proyecto/<id>',mod_proyects,name="mod_proyectos"),
    path('eliminar_proyecto/<id>',del_proyects,name="del_proyectos"),
    path('quienes-somos/', qsomos, name="qsomos")
]

#para que muestre la imagen
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)