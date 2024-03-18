from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def registro_materias(request):
    return render(request, 'registro_materia.html')

def malla_curricular(request):
    return render(request, 'np_malla_curricular.html')

def nuevo_programa(request):
    if request.method =='GET':
        return render(request, 'nuevo_programa.html')
    else:
        Programa_de_posgrado.objects.create(nombre=request.POST['nombre'], codigo=request.POST['codigo'],
                                            descripcion=request.POST['descripcion'], fecha_inicio=request.POST['fecha_inicio'],
                                            fecha_finalizacion=request.POST['fecha_finalizacion'], value=request.POST['value'],
                                            duracion=request.POST['duracion'], modalidad=request.POST['modalidad'])
        return redirect('/gestion/nuevoprograma/mallacurricular')
def gestion(request):
    return render(request, 'gestion.html')

def empezar_pogra(request):
    return render(request, 'empezar_progra.html')
        

def log_in(request):
    return render(request, 'log_in.html')

def register_us(request):
    if request.method =='GET':
        return render(request, 'register_us.html',{
        'form' : NewUsuary()    
        
    })
    else:
        Usuario.objects.create(nombre=request.POST['nombre'], codigo=request.POST['codigo'], 
        rol=request.POST['rol'], departamento=request.POST['departamento'],
        correo_electronico=request.POST['nombre'], telefono=request.POST['telefono'])
        return redirect('/')


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def asignar_espacios(request):
    return render(request, 'asignar_espacios.html')