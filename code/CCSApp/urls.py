from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.log_in),
    path('register_us/', views.register_us),
    path('index/', views.index, name='index'),  
    path('index/programacion/', views.empezar_progra, name ="empezar_progra"),
    path('index/gestion/', views.gestion),
    path('index/gestion/nuevoprograma/', views.nuevo_programa),
    path('gestion/nuevoprograma/director_programa/', views.director_programa),
    path('gestion/nuevoprograma/mallacurricular/', views.malla_curricular),
    path('gestion/nuevoprograma/operacion_exitosa/', views.operacionexitosanp),
    path('gestion/eliminar_programa_inactivo/', views.eliminar_programa_inactivo, name = 'eliminar_programa'),
    path('index/servicios_asignacion/asignar_horario/', views.asignar_horario),
    path('index/servicios_asignacion/modificar_horarios/', views.modificar_horarios),
    path('index/servicios_asignacion/consultar_horarios/', views.consultar_horarios),
    path('index/servicios_asignacion/', views.servicios_asignacion),
    path('index/servicios_asignacion/registroMateria/', views.registrar_materia_malla),
    path('index/servicios_asignacion/buscar_materia/', views.buscar_materia, name='buscar_materia'),
    path('index/servicios_asignacion/buscar_materia/editar/<str:nombre_materia>/', views.editar_materia, name='editar_materia'),
    path('index/servicios_asignacion/registroProfesor/', views.registrar_profesor),
    path('index/servicios_asignacion/buscar_profesor/', views.buscar_profesor, name='buscar_profesor'),
    path('index/servicios_asignacion/buscar_profesor/editar/<str:nombre_profesor>/', views.editar_profesor, name='editar_profesor'),

    #path('gestion/nuevoprograma/mallacurricular/registroMaterias/', views.registro_materias),
    path('index/lista/', views.lista_programas, name='lista_programas'),
    path('index/gestion/editar/<str:codigo>/', views.editar_programa, name='editar_programa'),
    path('programacion/materias/<int:programa_id>/', views.materias, name='materias'),
    path('programacion/materias/<int:materia_id>/horarios/', views.horarios, name='horarios'),
    
    path('delete_program/<str:codigo>',views.delete_program,name = 'delete-program'),
    path('index/program_csv/', views.programs_csv, name = 'program-csv'),
    path('index/servicios_asignacion/crear_espacio/', views.crear_espacio, name="crear_espacio"),
    path('crear_edificio/', views.crear_edificio, name="crear_edificio"),
    
    path('index/servicios_asignacion/lista_edificios/', views.lista_edificios, name='lista_edificios'),
    path('index/servicios/asignacion/lista_espacios/<str:nombre_edificio>/', views.lista_espacios, name='lista_espacios'),
    path('index/servicios_asignacion/editar_espacio/<str:espacio_codigo>/', views.editar_espacio, name='editar_espacio')
    ]
