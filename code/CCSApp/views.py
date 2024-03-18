from django.shortcuts import render, redirect
from django.http import HttpResponse
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
            return redirect('/servicios_asignacion')  # Cambia esta URL por la adecuada
    else:
        form = NewHorario()

    return render(request, 'asignar_horario.html', {'form': form})

def servicios_asignacion(request):
    return render(request, 'servicios_asignacion.html')

def malla_curricular(request):
    return render(request, 'np_malla_curricular.html')

def nuevo_programa(request):
    return render(request, 'nuevo_programa.html')

def gestion(request):
    return render(request, 'gestion.html')

def empezar_pogra(request):
    return render(request, 'empezar_progra.html')

def log_in(request):
    return render(request, 'log_in.html')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
