from django.contrib import admin
from django.urls import path, include
from .views import index,formulario,formulario_insumo,galeria,login,quienes_somos,servicios,ubicacion,cerrarSesion,listar_insumos,eliminar_insumo,buscar_insumo,modificar_insumo


urlpatterns = [
    path('',index,name='INDEX'),
    path('formulario/',formulario,name='FORMULARIO'),
    path('formulario_insumo/',formulario_insumo,name='FORMULARIO_INSUMO'),
    path('formulario_insumo_listar/',listar_insumos,name='LISTAR'),
    path('eliminar_in/<id>/',eliminar_insumo,name='ELIMINAR'),
    path('buscar_in/<id>/',buscar_insumo,name='BUSCAR'),
    path('modificar/',modificar_insumo,name='MODIFICAR'),
    
    path('galeria/',galeria,name='GALERIA'),
    
    path('login/',login,name='LOGIN'),
    path('logout/',cerrarSesion,name='LOGOUT'),
    
    path('quienes_somos/',quienes_somos,name='QUIENES_SOMOS'),
    path('servicios/',servicios,name='SERVICIOS'),
    path('ubicacion/',ubicacion,name='UBICACION'),

]

