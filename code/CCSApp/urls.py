from django.urls import path
from . import views
urlpatterns = [
    path('', views.log_in),
    path('index/', views.index),
    path('pogramacion/', views.empezar_pogra),
    path('gestion/', views.gestion)

]