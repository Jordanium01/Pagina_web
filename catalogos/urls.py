import statistics
from django.urls import path, include
from.views import home, faq, contacts, proyects, qsomos, login, regis, form_proyects, mod_proyects, del_proyects, estadisticas, mod_statis, estadistica_individual, form_statis, del_statis
from django.conf import settings
from django.conf.urls.static import static
from estadisticas.views import lista_Clasificacion
from django.contrib.auth.views import LogoutView,logout_then_login

urlpatterns = [
    #path('', funcion, alias)
    path('', home,name="index"),
    path('contacto/', contacts, name="contacto"),
    path('faq/', faq, name="faq"),
    path('login/', login, name="login"),
    path('register/', regis, name="register"),
    path('proyectos/', proyects, name="proyectos"),
    path('formulario_proyectos/',form_proyects,name="fom_proyectos"),
    path('modificar_proyecto/<id>',mod_proyects,name="mod_proyectos"),
    path('eliminar_proyecto/<id>',del_proyects,name="del_proyectos"),
    
    path('estadisticas_generales/', estadisticas, name="estadisticas"),
    path('registro_estadistica/',form_statis,name="form_estadistica"),
    path('estadistica/<id>', estadistica_individual, name="estadistica_individual"),
    path('modificacion_estadistica/<id>', mod_statis, name="mod_estadisticas"),
    path('eliminar_estadistica/<id>',del_statis,name="del_estadistica"),

    
    path('quienes-somos/', qsomos, name="qsomos"),
    path('', LogoutView.as_view(),name='logout'),
    path('api/', include('estadisticas.urls')),
    
    path('sigin/', include('usuario.urls')),
]

#para que muestre la imagen
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)