from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *

# Create your views here.

def asignar_horario(request):
    if request.method == 'POST':
        form = NewHorario(request.POST)
        if form.is_valid():
            # Guardar el objeto Horario en la base de datos
            fecha_hora = form.cleaned_data['fecha_hora']
            profesor = form.cleaned_data['profesor']
            materia = form.cleaned_data['materia']
            modalidad = form.cleaned_data['modalidad']
            enlace_virtual = form.cleaned_data['enlace_virtual']
            salon_presencial = form.cleaned_data['salon_presencial']
            horario = Horario.objects.create(fecha_hora=fecha_hora, profesor=profesor, materia=materia,
                                              modalidad=modalidad, enlace_virtual=enlace_virtual,
                                              salon_presencial=salon_presencial)
            # Redirigir a la página de éxito o a donde sea necesario
            return redirect('/servicios_asignacion')  
    else:
        form = NewHorario()

    return render(request, 'asignar_horario.html', {'formNewHorario': form})

def modificar_horarios(request):
    return render(request, 'modificar_horarios.html')

def consultar_horarios(request):
    return render(request, 'consultar_horarios.html')

def servicios_asignacion(request):
    return render(request, 'servicios_asignacion.html')

def registrar_materia_malla(request):
    if request.method == "GET":
        return render(request, 'registro_materia.html', {
            'form': CrearMateria
        })
    else:
        try:
            form = CrearMateria(request.POST)
            if form.is_valid():
                materia = Materia(
                    nombre=form.cleaned_data['nombre'],
                    codigo=form.cleaned_data['codigo'],
                    descripcion=form.cleaned_data['descripcion'],
                    creditos=form.cleaned_data['creditos'],
                    syllabus=form.cleaned_data['syllabus'],)
                materia.save()
                return redirect('/index')
        except ValueError:
            return render(request, 'registro_materia.html', {
            'form': CrearMateria,
            'error': 'Please provide valid data'
            })
        
def registro_materias(request):
    if request.method == 'POST':
        form = CrearMateria(request.POST)
        if form.is_valid():
            materia = Materia(
                nombre=form.cleaned_data['nombre'],
                codigo=form.cleaned_data['codigo'],
                descripcion=form.cleaned_data['descripcion'],
                creditos=form.cleaned_data['creditos'],
                syllabus=form.cleaned_data['syllabus'],)
            materia.save()
            return redirect('/index') 
    else:
        form = CrearMateria()
    return render(request, 'registro_materia.html', {'form' : form})

def malla_curricular(request):
    if request.method == 'POST':
        form = CrearMallaCurricular(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario y guardar el programa académico
            malla_curricular = Malla_curricular(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                requisitos_previos=form.cleaned_data['requisitos_previos'],
                programa_de_posgrado=form.cleaned_data['programa_de_posgrado'],)
            malla_curricular.save()
            return redirect('/gestion/nuevoprograma/mallacurricular/registroMaterias')  # Redirigir a alguna vista después de guardar el formulario
    else:
        form = CrearMallaCurricular()
    return render(request, 'np_malla_curricular.html', {'form' : form})

def nuevo_programa(request):
    if request.method == 'POST':
        form = CrearProgramaAcademico(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario y guardar el programa académico
            programa_academico = Programa_de_posgrado(
                name=form.cleaned_data['name'],
                codigo=form.cleaned_data['codigo'],
                descripcion=form.cleaned_data['descripcion'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_finalizacion=form.cleaned_data['fecha_finalizacion'],
                value=form.cleaned_data['value'],
                duracion=form.cleaned_data['duracion'],
                facultad=form.cleaned_data['facultad'],
                modalidad=form.cleaned_data['modalidad'])
            programa_academico.save()
            return redirect('/gestion/nuevoprograma/mallacurricular')  # Redirigir a alguna vista después de guardar el formulario
    else:
        form = CrearProgramaAcademico()
    return render(request, 'nuevo_programa.html', {'form': form})

def empezar_pogra(request):
    return render(request, 'empezar_progra.html')
        

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            correo_electronico = form.cleaned_data['correo_electronico']
            try:
                usuario = Usuario.objects.get(codigo=codigo, correo_electronico=correo_electronico)
                # Autenticación exitosa, puedes redirigir a una página de inicio o hacer cualquier otra cosa que necesites.
                # Por ejemplo:
                # return redirect('inicio')  # Cambia 'inicio' con el nombre de tu URL de inicio.
                return render(request, 'index.html', {'usuario': usuario})
            except Usuario.DoesNotExist:
                # Si no se encuentra el usuario, puedes mostrar un mensaje de error o redirigir de nuevo al formulario de inicio de sesión.
                form.add_error(None, 'Código o correo electrónico incorrecto')
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
        correo_electronico=request.POST['correo_electronico'], telefono=request.POST['telefono'])
        return redirect('/')


def gestion(request):
    return render(request, 'gestion.html')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def asignar_espacios(request):
    return render(request, 'asignar_espacios.html')