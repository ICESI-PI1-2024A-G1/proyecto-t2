from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    #Experimental
    path('api/filtrar_materias/', views.filtrar_materias, name='filtrar_materias'),
    
    path('', views.log_in),
    path('register_us/', views.register_us),
    path('index/', views.index, name='index'),  
    path('index/programacion/', views.crear_programacion_academica, name = "crear_programacion_academica"),
    path('index/gestion/', views.gestion),
    
    path('gestion/nuevoprograma/director_programa/', views.director_programa),
    path('gestion/nuevoprograma/mallacurricular/', views.malla_curricular),
    path('gestion/nuevoprograma/operacion_exitosa/', views.operacionexitosanp),
    path('gestion/eliminar_programa_inactivo/', views.eliminar_programa_inactivo, name = 'eliminar_programa'),
    path('index/servicios_asignacion/modificar_horarios/', views.modificar_horarios),
    path('index/servicios_asignacion/modificar_horarios/<int:id_horario>/', views.modificar_horarios, name='modificar_horarios'),
    path('index/servicios_asignacion/consultar_horarios/', views.consultar_horarios),
    path('index/servicios_asignacion/', views.servicios_asignacion),
    path('index/servicios_asignacion/registroMateria/', views.registrar_materia_malla),
    path('index/servicios_asignacion/buscar_materia/', views.buscar_materia, name='buscar_materia'),
    path('index/servicios_asignacion/buscar_materia/editar/<str:nombre_materia>/', views.editar_materia, name='editar_materia'),
    path('index/servicios_asignacion/registroProfesor/', views.registrar_profesor),
    path('index/servicios_asignacion/buscar_profesor/', views.buscar_profesor, name='buscar_profesor'),
    path('index/servicios_asignacion/buscar_profesor/editar/<str:nombre_profesor>/', views.editar_profesor, name='editar_profesor'),
    path('index/gestion/nuevoprograma/', views.nuevo_programa),
    path('index/gestion/buscar_programa_academico/', views.buscar_programa_academico, name='buscar_programa_academico'),
    path('index/gestion/buscar_programa_academico/editar/<str:codigo_programa>/', views.editar_programa, name='editar_programa'),
    path('index/gestion/eliminar_programa_academico/', views.consultar_programas_academicos),
    
    path('index/lista/', views.lista_programas, name='lista_programas'),
   
    path('programacion/materias/<int:materia_id>/horarios/', views.horarios, name='horarios'),
    
    path('delete_program/<str:codigo>',views.delete_program,name = 'delete-program'),
    path('index/programacion/program_csv/', views.InformeProgramacion.as_view(), name = 'program-csv'),
    path('index/programacion/asignar_horario/', views.asignar_horario),
    path('index/servicios_asignacion/crear_espacio/', views.crear_espacio, name="crear_espacio"),
    path('index/servicios_asignacion/crear_evento/', views.crear_evento, name="crear_evento"),
    path('index/servicios_asignacion/crear_actividad/', views.crear_actividad, name="crear_actividad"),
    path('crear_edificio/', views.crear_edificio, name="crear_edificio"),
    
    path('index/servicios_asignacion/lista_edificios/', views.lista_edificios, name='lista_edificios'),
    path('index/servicios/asignacion/lista_espacios/<str:nombre_edificio>/', views.lista_espacios, name='lista_espacios'),
    path('index/servicios_asignacion/editar_espacio/<str:espacio_codigo>/', views.editar_espacio, name='editar_espacio'),

    path('index/gestion/programas_csv/', views.programas_csv, name = 'programas-csv'),
    path('index/gestion/eliminar_programa_academico/<int:codigo_programa>/', views.eliminar_programa_inactivo, name='eliminar_programa_inactivo')
    ]
