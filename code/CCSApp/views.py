from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import csv
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from django.db.models import Q

# Create your views here.

def asignar_horario(request):
    if request.method == 'POST':
        form = NewHorario(request.POST)
        if form.is_valid():
            id_horario = form.cleaned_data['id_horario']
            fecha_inicio_hora = form.cleaned_data['fecha_inicio_hora']
            fecha_final_hora = form.cleaned_data['fecha_final_hora']
            modalidad = form.cleaned_data['modalidad']
            enlace_virtual = form.cleaned_data['enlace_virtual']
            salon_presencial = form.cleaned_data['espacio']
            materia = form.cleaned_data['materia']
            grupo = form.cleaned_data['grupo']

            # Verificar si hay algún horario existente que tenga conflicto con el nuevo horario
            conflicto = Horario.objects.filter(
                Q(salon_presencial=salon_presencial) &
                (
                    Q(fecha_inicio_hora__lte=fecha_inicio_hora, fecha_final_hora__gte=fecha_inicio_hora) |
                    Q(fecha_inicio_hora__lte=fecha_final_hora, fecha_final_hora__gte=fecha_final_hora) |
                    Q(fecha_inicio_hora__gte=fecha_inicio_hora, fecha_final_hora__lte=fecha_final_hora)
                )
            ).exists()

            if not conflicto:
                # No hay conflicto, guardar el nuevo horario en la base de datos
                horario = Horario.objects.create(id_horario = id_horario, fecha_inicio_hora=fecha_inicio_hora, fecha_final_hora = fecha_final_hora, materia=materia,
                                              modalidad=modalidad, enlace_virtual=enlace_virtual,
                                              salon_presencial=salon_presencial, grupo = grupo)
                return redirect('/index/servicios_asignacion')
            else:
                # Hay conflicto, mostrar un mensaje de error o manejar la situación adecuadamente
                form.add_error(None, "El horario se superpone con otro horario existente.")
        # Si el formulario no es válido, se volverá a renderizar con los errores
    else:
        form = NewHorario()

    return render(request, 'asignar_horario.html', {'formNewHorario': form})

def modificar_horarios(request):
    if request.method == 'POST':
        form = ModificarHorarioForm(request.POST)
        if form.is_valid():
            horario_id = form.cleaned_data['horario_id']
            horario = Horario.objects.get(pk=horario_id)
            horario.fecha_inicio_hora = form.cleaned_data['fecha_i_hora']
            horario.fecha_final_hora = form.cleaned_data['fecha_f_hora']
            horario.materia = form.cleaned_data['materia']
            horario.modalidad = form.cleaned_data['modalidad']
            horario.grupo = form.cleaned_data['grupo']
            horario.enlace_virtual = form.cleaned_data['enlace_virtual']
            horario.salon_presencial = form.cleaned_data['espacio']
            horario.save()
            return redirect('/index/servicios_asignacion') 
    else:
        form = ModificarHorarioForm()
    return render(request, 'modificar_horarios.html', {'formModificarHorarios': form})

def consultar_horarios(request):
    # Obtener todos los horarios inicialmente
    horarios = Horario.objects.all()

    # Obtener parámetros de filtro del formulario si están presentes en la solicitud GET
    modalidad = request.GET.get('modalidad')
    materia = request.GET.get('materia')
    grupo = request.GET.get('grupo')
    fecha_inicio_hora = request.GET.get('fecha_inicio')
    fecha_final_hora = request.GET.get('fecha_final')

    # Aplicar filtros según los parámetros proporcionados en el formulario
    if modalidad:
        horarios = horarios.filter(modalidad=modalidad)
    if materia:
        horarios = horarios.filter(materia=materia)
    if grupo:
        horarios = horarios.filter(grupo=grupo)
    if fecha_inicio_hora:
        horarios = horarios.filter(fecha_inicio_hora=fecha_inicio_hora)
    if fecha_final_hora:
        horarios = horarios.filter(fecha_final_hora=fecha_final_hora)

    # Pasar los horarios filtrados al contexto para mostrar en la plantilla
    context = {
        'horarios': horarios
    }

    return render(request, 'consultar_horarios.html', context)

def servicios_asignacion(request):
    if request.method == "GET":
        return render(request, 'servicios_asignacion.html')
    
from .models import Materia  # Asegúrate de importar el modelo Materia

def registrar_materia_malla(request):
    if request.method == "GET":
        return render(request, 'registro_materia.html', {
            'form': CrearMateria
        })
    else:
        try:
            form = CrearMateria(request.POST, request.FILES)
            if form.is_valid():
                codigo_materia = form.cleaned_data['codigo_materia']
                # Verificar si ya existe una materia con el mismo código
                if Materia.objects.filter(codigo_materia=codigo_materia).exists():
                    # Si existe, puedes manejar la situación como desees,
                    # por ejemplo, mostrando un mensaje de error
                    return render(request, 'registro_materia.html', {
                        'form': CrearMateria,
                        'error': 'La materia ya existe en la base de datos.'
                    })
                else:
                    syllabus_file = form.cleaned_data['syllabus']
                    if not syllabus_file.name.endswith('.pdf'):
                        raise ValidationError('El archivo debe ser un PDF.')

                    # Si no existe, crear la nueva materia
                    materia = Materia(
                        nombre_materia=form.cleaned_data['nombre_materia'],
                        codigo_materia=codigo_materia,
                        departamento=form.cleaned_data['departamento'],
                        creditos_materia=form.cleaned_data['creditos_materia'],
                        syllabus=syllabus_file
                    )
                    materia.save()
                    return redirect('/index/servicios_asignacion')
        except ValueError:
            return render(request, 'registro_materia.html', {
                'form': CrearMateria,
                'error': 'Por favor, proporcione datos válidos.'
            })

def buscar_materia(request):
    if request.method == 'POST':
        form = MateriaSearchForm(request.POST)
        if form.is_valid():
            nombre_materia = form.cleaned_data['nombre_materia']
            materias = Materia.objects.filter(nombre_materia__istartswith=nombre_materia)
            return render(request, 'buscar_materia.html', {'form': form, 'materias': materias})
    else:
        form = MateriaSearchForm()
    return render(request, 'buscar_materia.html', {'form': form})

def editar_materia(request, nombre_materia):
    materia = Materia.objects.get(nombre_materia=nombre_materia)
    if request.method == 'POST':
        form = MateriaEditForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('buscar_materia')
    else:
        form = MateriaEditForm(instance=materia)
    return render(request, 'editar_materia.html', {'form': form})

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
            return redirect('/index/servicios_asignacion/registroMateria')  # Redirigir a alguna vista después de guardar el formulario
    else:
        form = CrearMallaCurricular()
    return render(request, 'np_malla_curricular.html', {'form' : form})

def nuevo_programa(request):
    if request.method == 'POST':
        form = CrearProgramaAcademico(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario y guardar el programa académico
            programa_academico = Programa_de_posgrado(
                nombre_programa =form.cleaned_data['nombre_programa'],
                codigo_programa=form.cleaned_data['codigo_programa'],
                fecha_inicio_programa =form.cleaned_data['fecha_inicio_programa'],
                estado_programa = form.cleaned_data['estado_programa'],
                duracion_programa =form.cleaned_data['duracion_programa'],
                facultad_programa =form.cleaned_data['facultad_programa'],
                modalidad_programa =form.cleaned_data['modalidad_programa'])
            programa_academico.save()
            return redirect('/gestion/nuevoprograma/director_programa')  # Redirigir a alguna vista después de guardar el formulario
    else:
        form = CrearProgramaAcademico()
    return render(request, 'nuevo_programa.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cedula = form.cleaned_data['cedula']
            clave = form.cleaned_data['password']
            user = authenticate(request, cedula=cedula, password=clave)
            try:
                usuario = Usuario.objects.get(cedula=cedula, password=clave)
                # Autenticación exitosa, puedes redirigir a una página de inicio o hacer cualquier otra cosa que necesites.
                # Por ejemplo:
                # return redirect('inicio')  # Cambia 'inicio' con el nombre de tu URL de inicio.
                return redirect(index)
            except Usuario.DoesNotExist:
                # Si no se encuentra el usuario, puedes mostrar un mensaje de error o redirigir de nuevo al formulario de inicio de sesión.
                form.add_error(None, 'Usuario o clave incorrecta, intente de nuevo')
    else:
        form = LoginForm()
    return render(request, 'log_in.html', {'form': form})

def register_us(request):
    if request.method == 'POST':
        form = NewUsuary(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            cedula = form.cleaned_data['cedula']
            rol = form.cleaned_data['rol']
            departamento = form.cleaned_data['departamento']
            correo_electronico = form.cleaned_data['correo_electronico']
            telefono = form.cleaned_data['telefono']
            password = form.cleaned_data['password']
            # hashed_password = make_password(password)
            
            # Verificar si ya existe un usuario con la cédula proporcionada
            if Usuario.objects.filter(cedula=cedula).exists():
                # Manejar el caso donde ya existe un usuario con la cédula proporcionada
                # Por ejemplo, puedes agregar un mensaje de error al formulario.
                return render(request, 'register_us.html', {
                        'form': NewUsuary,
                        'error': 'Ya existe un usuario con esta cédula.'
                })
            else:
                # Crear un nuevo usuario con los datos proporcionados
                Usuario.objects.create(
                nombre=nombre,
                cedula=cedula,
                rol=rol,
                departamento=departamento,
                correo_electronico=correo_electronico,
                telefono=telefono,
                password=password
            )
            # Redirigir a la página principal después del registro exitoso
            return redirect('/')
        # Resto del código para manejar el caso cuando el formulario no es válido
        # ...
    else:
        form = NewUsuary()
    return render(request, 'register_us.html', {'form': form})


def gestion(request):
    return render(request, 'gestion.html')


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    
def home(request):
    return render(request, 'home.html')

def asignar_espacios(request):
    return render(request, 'asignar_espacios.html')

def registrar_profesor(request):
    if request.method == "POST":
        form = RegistrarProfesor(request.POST)
        if form.is_valid():
            nombre_profesor = form.cleaned_data['nombre_profesor']
            cedula_profesor = form.cleaned_data['cedula_profesor']
            especializacion_profesor = form.cleaned_data['especializacion_profesor']
            correo_electronico = form.cleaned_data['correo_electronico']
            telefono = form.cleaned_data['telefono']
            
            if Profesor.objects.filter(cedula_profesor=cedula_profesor).exists():
                return render(request, 'registro_profesores.html', {
                    'form': form,
                    'error': 'El profesor ya existe en la base de datos.'
                })
            else:
                profesor = Profesor(
                    nombre_profesor=nombre_profesor,
                    cedula_profesor=cedula_profesor,
                    especializacion_profesor=especializacion_profesor,
                    correo_electronico=correo_electronico,
                    telefono=telefono,
                )
                profesor.save()
                return redirect('/index')
    else:
        form = RegistrarProfesor()
    
    return render(request, 'registro_profesores.html', {
        'form': form
    })

def buscar_profesor(request):
    if request.method == 'POST':
        form = ProfesorSearchForm(request.POST)
        if form.is_valid():
            nombre_profesor = form.cleaned_data['nombre_profesor']
            profesores = Profesor.objects.filter(nombre_profesor__icontains=nombre_profesor)
            return render(request, 'buscar_profesor.html', {'form': form, 'profesores': profesores})
    else:
        form = ProfesorSearchForm()
    return render(request, 'buscar_profesor.html', {'form': form})

def editar_profesor(request, nombre_profesor):
    profesor = Profesor.objects.get(nombre_profesor=nombre_profesor)
    if request.method == 'POST':
        form = ProfesorEditForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('buscar_profesor')
    else:
        form = ProfesorEditForm(instance=profesor)
    return render(request, 'editar_profesor.html', {'form': form})

def lista_programas(request):
    programas = Programa_de_posgrado.objects.all()
    directores = Director_de_programa.objects.all()
    return render(request, 'lista_programas.html', {'programas': programas, 'directores': directores})

def editar_programa(request, codigo_programa):  
    programa = get_object_or_404(Programa_de_posgrado, codigo_programa=codigo_programa)  
    form = EditarProgramaForm(request.POST, instance=programa)
    if form.is_valid():
        form.save()
        return redirect('lista_programas_pos.html')  
    else:
        form = EditarProgramaForm(instance=programa)
    return render(request, 'editar_programa.html', {'form': form})

def director_programa(request):
    if request.method == 'POST':
        form = DirectorDePrograma(request.POST, request.FILES)
        if form.is_valid():
            # Procesar los datos del formulario y guardar el programa académico
            director_programa = Director_de_programa(
                nombre_director=form.cleaned_data['nombre_director'],
                numero_director=form.cleaned_data['numero_director'],
                correo_director=form.cleaned_data['correo_director'],
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
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=programasdeposgrado.xlsx'

    # Crear un nuevo libro de trabajo
    wb = Workbook()
    # Seleccionar la hoja activa
    ws = wb.active

    # Escribir el encabezado
    headers = ['PROGRAMA', 'COD BANNER', 'DEPT', 'HORAS', 'NUM. CREDITOS', 'PERIODO', 'MATERIA', 'MODALIDAD', 'GRUPO', 'DOCENTE', 'C.C', 'TIPO DE CONTRATO', 'CIUDAD', 'EMAIL', 'TELEFONO', 'FECHA DE CLASE', 'HORARIO', 'ESTADO DE CONTRATO', 'FECHA ELAB. DE CONTRATO', 'No. CONTRATO', 'LISTAS - MOSAICOS', 'ENTREGA DE NOTAS', 'INTU/CANVAS', 'TIQUETES', 'HOTEL', 'VIATICOS']
    ws.append(headers)

    # Iterar sobre los programas y escribir los datos en el archivo Excel
    # programas = Programa_de_posgrado.objects.all()
    # for programa in programas:
    #     row_data = [programa.name, programa.codigo, programa.descripcion, programa.fecha_inicio, programa.fecha_finalizacion, programa.estado, programa.duracion, programa.facultad]
    #     ws.append(row_data)

    # Aplicar color a las celdas de los encabezados
    for cell in ws[1]:
        cell.fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

    # Obtener el índice de la columna "GRUPO" en la hoja de cálculo
    grupo_index = headers.index('GRUPO') + 1

    # Aplicar color verde a las celdas de la columna "GRUPO"
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=grupo_index, max_col=grupo_index):
        for cell in row:
            cell.fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")

    # Agregar bordes a todas las celdas
    border = Border(left=Side(style='thin'), 
                    right=Side(style='thin'), 
                    top=Side(style='thin'), 
                    bottom=Side(style='thin'))
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=len(headers)):
        for cell in row:
            cell.border = border

    # Ajustar el ancho de las columnas al contenido
    for column in ws.columns:
        max_length = 0
        column_letter = get_column_letter(column[0].column)  # Obtener la letra de la columna
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2  # Multiplicar por 1.2 para dar un poco de espacio adicional
        ws.column_dimensions[column_letter].width = adjusted_width

    # Guardar el libro de trabajo en el flujo de respuesta
    wb.save(response)
    return response




def materias(request):
    programas = Programa_de_posgrado.objects.all()
    materias = Materia.objects.all()
    context = {'programas': programas, 'materias': materias}
    return render(request, 'materias.html', context)

def horarios(request, codigo_materia):
    horarios = Horario.objects.filter(materia__codigo=codigo_materia)
    context = {'horarios': horarios}
    return render(request, 'lista_horarios.html', context)


def elegir_semestre(request):
    semestre = Semestre.objects.all()
    context = { 'semestres': semestre }

    return render(request, "elegir_semestre.html", context)

def crear_espacio(request):
    if request.method == 'POST':
        form = EspacioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/servicios_asignacion')  
    else:
        form = EspacioForm()
    return render(request, 'crear_espacio.html', {'form': form})

def crear_espacio(request):
    if request.method == 'POST':
        form = EspacioForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario y guardar el programa académico
            espacio = Espacio(
                espacio_codigo=form.cleaned_data['espacio_codigo'],
                capacidad_espacio=form.cleaned_data['capacidad_espacio'],
                edificio_espacio=form.cleaned_data['edificio_espacio'],
                disponibilidad_espacio=form.cleaned_data['disponibilidad_espacio'],
                tipo=form.cleaned_data['tipo'])
            espacio.save()
            return redirect('/index/servicios_asignacion')  # Redirigir a alguna vista después de guardar el formulario
    else:
        form = EspacioForm()
    return render(request, 'crear_espacio.html', {'form': form})

def crear_edificio(request):
    if request.method == 'POST':
        form = CrearEdificio(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/servicios_asignacion')  
    else:
        form = CrearEdificio()
    return render(request, 'crear_edificio.html', {'form': form})

def lista_edificios(request):
    edificios = Edificio.objects.all()
    return render(request, 'lista_edificios.html', {'edificios': edificios})

def lista_espacios(request, nombre_edificio):
    edificio = get_object_or_404(Edificio, pk=nombre_edificio)
    espacios = Espacio.objects.filter(edificio_espacio=edificio)
    return render(request, 'lista_espacios.html', {'edificio': edificio, 'espacios': espacios})

def editar_espacio(request, espacio_codigo):
    espacio = get_object_or_404(Espacio, pk=espacio_codigo)
    if request.method == 'POST':
        form = EditarEspacio(request.POST, instance=espacio)
        if form.is_valid():
            form.save()
            return redirect('/index/servicios_asignacion')  # Redirigir a la lista de edificios después de la edición
    else:
        form = EditarEspacio(instance=espacio)
    return render(request, 'editar_espacio.html', {'form': form})

def crear_programacion_academica(request):
    form = ProgramacionAcademicaForm(request.POST or None)  # Maneja datos del POST
    if form.is_valid():
        programa_de_posgrado = form.cleaned_data['programa_de_posgrado']
        semestres = Semestre.objects.filter(programa_semestre = programa_de_posgrado)
        departamento = form.cleaned_data['departamento']
    else:
        programa_de_posgrado = None
        semestres = []
        departamento = None

    context = {'form': form, 
               'programa_de_posgrado': programa_de_posgrado, 
               'semestres': semestres,
               'departamento': departamento}
    
    return render(request, 'programacion_academica.html', context)

def crear_evento(request):
    if request.method == 'POST':
        formEvent = EventoForm(request.POST)
        if formEvent.is_valid():
            # Procesar los datos del formulario y guardar el programa académico
            evento = Evento(
                nombre_evento=formEvent.cleaned_data['nombre_evento'],
                fecha_inicio_evento=formEvent.cleaned_data['fecha_inicio_evento'],
                fecha_finalizacion_evento=formEvent.cleaned_data['fecha_finalizacion_evento'],
                lugar_evento=formEvent.cleaned_data['lugar_evento'],
                descripcion_evento=formEvent.cleaned_data['descripcion_evento'],
                programa_de_posgrado_evento=formEvent.cleaned_data['programa_de_posgrado_evento'])
            evento.save()
            return redirect('/index/servicios_asignacion')  # Redirigir a alguna vista después de guardar el formulario
    else:
        formEvent = EventoForm()
    return render(request, 'crear_evento.html', {'formEvent': formEvent})

def crear_actividad(request):
    if request.method == 'POST':
        formActividad = ActividadForm(request.POST)
        if formActividad.is_valid():
            # Procesar los datos del formulario y guardar el programa académico
            actividad = Actividad(
                nombre_actividad=formActividad.cleaned_data['nombre_actividad'],
                duracion_en_horas=formActividad.cleaned_data['duracion_en_horas'],
                orador_actividad=formActividad.cleaned_data['orador_actividad'],
                evento_actividad=formActividad.cleaned_data['evento_actividad'])
            actividad.save()
            return redirect('/index/servicios_asignacion')  # Redirigir a alguna vista después de guardar el formulario
    else:
        formActividad = ActividadForm()
    return render(request, 'crear_actividad.html', {'formActividad': formActividad})
