from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.log_in),
    path('register_us/', views.register_us),
    path('index/', views.index),
    path('programacion/', views.empezar_pogra),
    path('gestion/', views.gestion),
    path('gestion/nuevoprograma/', views.nuevo_programa),
    path('gestion/nuevoprograma/director_programa/', views.director_programa),
    path('gestion/nuevoprograma/mallacurricular/', views.malla_curricular),
    path('gestion/nuevoprograma/operacion_exitosa/', views.operacionexitosanp),
    path('gestion/eliminar_programa_inactivo/', views.eliminar_programa_inactivo, name = 'eliminar_programa'),
    path('asignar_horario/', views.asignar_horario, name='asignar_horario'),
    path('modificar_horarios/', views.modificar_horarios, name='modificar_horarios'),
    path('consultar_horarios/', views.consultar_horarios, name='consultar_horarios'),
    path('servicios_asignacion/', views.servicios_asignacion),
    path('gestion/nuevoprograma/mallacurricular/registroMaterias/', views.registro_materias),
    path('lista/', views.lista_programas, name='lista_programas'),
    path('editar/<str:codigo>/', views.editar_programa, name='editar_programa'),
    path('index/edit/<str:codigo>/', views.edit_programacion, name='editar_programacion'),
    path('delete_program/<str:codigo>',views.delete_program,name = 'delete-program'),
    ]
