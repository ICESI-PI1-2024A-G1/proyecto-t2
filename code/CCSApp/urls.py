from django.urls import path
from . import views
urlpatterns = [
    path('', views.log_in),
    path('index/', views.index),
    path('pogramacion/', views.empezar_pogra),
    path('gestion/', views.gestion),
    path('gestion/nuevoprograma/', views.nuevo_programa),
    path('gestion/nuevoprograma/mallacurricular/', views.malla_curricular),
    path('gestion/editarprograma/', views.editar_programa),
    path('gestion/eliminarprograma/', views.eliminar_programa),

]