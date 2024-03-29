from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.log_in),
    path('register_us/', views.register_us),
    path('index/', views.index),
    path('pogramacion/', views.empezar_pogra),
    path('asignar_horario/', views.asignar_horario, name='asignar_horario'),
    path('servicios_asignacion/', views.servicios_asignacion),
    
    # Urls de gestion 
    path('gestion/', views.gestion),
    path('gestion/nuevoprograma/', views.nuevo_programa),
    path('gestion/nuevoprograma/mallacurricular/', views.malla_curricular),
    path('gestion/nuevoprograma/mallacurricular/registroMaterias/', views.registro_materias),
    path('gestion/nuevoprograma/director_programa/', views.director_programa),

]