from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('asignar_horario/', views.asignar_horario, name='asignar_horario'),
    path('servicios_asignacion/', views.servicios_asignacion),  
]