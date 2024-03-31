from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *
import csv

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
            return redirect('/servicios_asignacion')  
    else:
        form = NewHorario()

    return render(request, 'asignar_horario.html', {'formNewHorario': form})

def modificar_horarios(request):
    if request.method == 'POST':
        form = ModificarHorarioForm(request.POST)
        if form.is_valid():
            horario_id = form.cleaned_data['horario_id']
            horario = Horario.objects.get(pk=horario_id)
            horario.fecha_hora = form.cleaned_data['fecha_hora']
            horario.profesor = form.cleaned_data['profesor']
            horario.materia = form.cleaned_data['materia']
            horario.modalidad = form.cleaned_data['modalidad']
            horario.enlace_virtual = form.cleaned_data['enlace_virtual']
            horario.salon_presencial = form.cleaned_data['salon_presencial']
            horario.save()
            return redirect('/servicios_asignacion') 
    else:
        form = ModificarHorarioForm()
    return render(request, 'modificar_horarios.html', {'formModificarHorarios': form})

def consultar_horarios(request):
    horarios = Horario.objects.all()
    return render(request, 'consultar_horarios.html', {'horarios': horarios})

def servicios_asignacion(request):
    return render(request, 'servicios_asignacion.html')

def registro_materias(request):
    if request.method == 'POST':
        form = CrearMateria(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario y guardar el programa académico
            materia = Materia(
                nombre=form.cleaned_data['nombre'],
                codigo=form.cleaned_data['codigo'],
                descripcion=form.cleaned_data['descripcion'],
                creditos=form.cleaned_data['creditos'],
                syllabus=form.cleaned_data['syllabus'],)
            materia.save()
            return redirect('/index')  # Redirigir a alguna vista después de guardar el formulario
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
                estado = form.cleaned_data['estado'],
                duracion=form.cleaned_data['duracion'],
                facultad=form.cleaned_data['facultad'],
                modalidad=form.cleaned_data['modalidad'])
            programa_academico.save()
            return redirect('/gestion/nuevoprograma/director_programa')  # Redirigir a alguna vista después de guardar el formulario
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

def lista_programas(request):
    programas = Programa_de_posgrado.objects.all()
    return render(request, 'lista_programas.html', {'programas': programas})

def editar_programa(request, codigo):  
    programa = get_object_or_404(Programa_de_posgrado, codigo=codigo)  
    form = EditarProgramaForm(request.POST, instance=programa)
    if form.is_valid():
        form.save()
        return redirect('lista_programas')  
    else:
        form = EditarProgramaForm(instance=programa)
    return render(request, 'editar_programa.html', {'form': form})

def director_programa(request):
    if request.method == 'POST':
        form = DirectorDePrograma(request.POST, request.FILES)
        if form.is_valid():
            # Procesar los datos del formulario y guardar el programa académico
            director_programa = Director_de_programa(
                nombre=form.cleaned_data['nombre'],
                numero=form.cleaned_data['numero'],
                correo=form.cleaned_data['correo'],
                descripcion_cargo=form.cleaned_data['descripcion_cargo'],
                foto_de_perfil=form.cleaned_data['foto_de_perfil'])

            # Guardar la foto
            with open(director_programa.foto_de_perfil.path, 'wb+') as f:
                for chunk in director_programa.foto_de_perfil.chunks():
                    f.write(chunk)

            director_programa.save()
            return redirect('/gestion/nuevoprograma/mallacurricular')  # Redirigir a alguna vista después de guardar el formulario
        else:
            form = DirectorDePrograma(request.POST)
    else:
        form = DirectorDePrograma()
    return render(request, 'director_programa.html', {'form': form})

def operacionexitosanp(request):
    return render(request, 'operacion_exitosa_np.html')

def eliminar_programa_inactivo(request):
    programas = Programa_de_posgrado.objects.all()
    return render(request, 'eliminar_programa_inactivo.html', {'programas': programas})

def delete_program(request, codigo):
    programa = Programa_de_posgrado.objects.get(pk = codigo)
    programa.delete()
    return redirect('eliminar_programa')

def programs_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename = programasdeposgrado.csv'

    writer = csv.writer(response)
    programas = Programa_de_posgrado.objects.all()

    writer.writerow(['Nombre del Programa', 'Codigo del programa', 'Descripcion', 'Fecha de Inicio', 'Fecha finalizacion', 'Estado', 'Duracion (Años)', 'Facultad', 'Modalidad'])

    for programa in programas:
        writer.writerow([programa.name, programa.codigo, programa.descripcion, programa.fecha_inicio, programa.fecha_finalizacion, programa.estado, programa.duracion, programa.facultad])

        
    return response


def edit_programacion(request, codigo):  
    programa = get_object_or_404(Programa_de_posgrado, codigo=codigo)  
    form = EditarProgramaForm(request.POST, instance=programa)
    if form.is_valid():
        form.save()
        return redirect('lista_programas')  
    else:
        form = EditarProgramaForm(instance=programa)
    return render(request, 'edit_programacion_semestral.html', {'form': form})
    