import statistics
from django.urls import path, include
from.views import home, faq, contacts, proyects, qsomos, login, regis, form_proyects, mod_proyects, del_proyects
from.views import estadisticas, mod_statis, estadistica_individual, form_statis, del_statis, tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, comprar, historial_compras, detalle_compra, aumentar_estado, disminuir_estado
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

    #Carrito de compra
    path('carrito/', tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('comprar/', comprar, name="buy"),
        #Historial de compra
    path('historial/', historial_compras, name="Historial"),
    path('detalle-compra/<id>', detalle_compra, name="Detalle-Compra"),

    path('estado_compra_sumar/<int:compra_id>/', aumentar_estado, name="sum_estado_compra"),
    path('estado_compra_restar/<int:compra_id>/', disminuir_estado, name="res_estado_compra"),

]

#para que muestre la imagen
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)