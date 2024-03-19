from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *

# Create your views here.
def registro_materias(request):
    return render(request, 'registro_materia.html')

def malla_curricular(request):
    return render(request, 'np_malla_curricular.html')

def nuevo_programa(request):
    if request.method =='GET':
        return render(request, 'nuevo_programa.html',{
            'nuevoPrograma' : CrearProgramaAcademico()            
        })
        
    else:
        Programa_de_posgrado.objects.create(name=request.POST['name'], codigo=request.POST['codigo'],
                                            descripcion=request.POST['descripcion'], fecha_inicio=request.POST['fecha_inicio'],
                                            fecha_finalizacion=request.POST['fecha_finalizacion'], value=request.POST['value'],
                                            duracion=request.POST['duracion'], facultad = request.POST['facultad'], modalidad=request.POST['modalidad'])
        return redirect('/gestion/nuevoprograma/mallacurricular')
def gestion(request):
    return render(request, 'gestion.html')

def empezar_pogra(request):
    return render(request, 'empezar_progra.html')
        

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            codigo = form.cleaned_data['codigo']
            
            user = Usuario.objects.filter(nombre=nombre, codigo=codigo).first()
            if user is not None:
                login(request, user)
                
                return redirect('/index')
            else:
          
                form.add_error(None, "Nombre de usuario o código incorrecto.")
    else:
        form = LoginForm()
    return render(request, 'log_in.html', {'form': form})

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