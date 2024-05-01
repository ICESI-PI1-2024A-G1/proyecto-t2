from django import forms
from .models import *


class RegistrarPeriodo(forms.Form):
    id_perido = forms.CharField(label = 'Id Periodo', max_length= 7, widget= forms.TextInput(attrs={'class': 'form-control'}))
    fecha_inicio_periodo = forms.DateField(label = "Fecha de inicio", widget = forms.DateTimeInput(attrs= {'type ' : 'date'}))
    fecha_final_periodo = forms.DateField(label = "Fecha de finalizacion", widget = forms.DateInput(attrs= {'type':'date'}))


class NewHorario(forms.Form):
    #id_horario = forms.CharField(label= "Id", max_length =255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_inicio_horario = forms.DateTimeField(
        label="Fecha Inicio",
        widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),
    )

    hora_inicio_horario = forms.TimeField(
        label="Hora Inicio",
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
    )
    hora_final_horario = forms.TimeField(
        label="Hora Final",
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
    )
    
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
        ('mixta', 'Mixta'),
    ]

    GRUPO = [
        ('001', '001'),
        ('002', '002'),
        ('003', '003'),
        ('004', '004')
    ]
    modalidad = forms.ChoiceField(label="Modalidad", choices=MODALIDAD_CHOICES, widget=forms.Select(attrs={'class': 'form-control2'}))
    enlace_virtual = forms.URLField(label="Enlace Virtual", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    espacio = forms.ModelChoiceField(label="Espacio", queryset=Espacio.objects.all(),empty_label=None, widget=forms.Select(attrs={'class': 'form-control2'}))
    materia = forms.ModelChoiceField(label="Materia", queryset=Materia.objects.all(),empty_label=None, widget=forms.Select(attrs={'class': 'form-control2'}))
    grupo = forms.ChoiceField(label="Grupo", choices=GRUPO, widget=forms.Select(attrs={'class': 'form-control2'}))
    
class ModificarHorarioForm(forms.Form):
    #horario_id = forms.ModelChoiceField(queryset=Horario.objects.all(), label="Selecciona un horario para modificar", widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_inicio_horario = forms.DateTimeField(
        label="Fecha Inicio",
        widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),
    )

    hora_inicio_horario = forms.TimeField(
        label="Hora Inicio",
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
    )
    hora_final_horario = forms.TimeField(
        label="Hora Final",
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
    )
    
    materia = forms.ModelChoiceField(label="Materia", queryset=Materia.objects.all(),empty_label=None, widget=forms.Select(attrs={'class': 'form-control2'}))
    
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
        ('mixta', 'Mixta'),
    ]

    GRUPO = [
        ('001', '001'),
        ('002', '002'),
        ('003', '003'),
        ('004', '004')
    ]
    modalidad = forms.ChoiceField(label="Nueva Modalidad", choices=MODALIDAD_CHOICES, widget=forms.Select(attrs={'class': 'form-control2'}))
    grupo = forms.ChoiceField(label="Nueva Grupo", choices=GRUPO, widget=forms.Select(attrs={'class': 'form-control2'}))
    enlace_virtual = forms.URLField(label="Nuevo Enlace Virtual", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    espacio = forms.CharField(label= "Espacio", max_length =255, widget=forms.Select(attrs={'class': 'form-control2'}))

    

class NewUsuary(forms.Form):
    nombre = forms.CharField(label= "nombre", max_length =255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cedula = forms.CharField(label= "cedula", max_length = 100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rol = forms.CharField(label= "rol", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    departamento = forms.CharField(label= "departamento", max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo_electronico = forms.EmailField(label="correo electronico", max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.IntegerField(label= "telefono", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class LoginForm(forms.Form):
    cedula = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CrearProgramaAcademico(forms.Form):
    nombre_programa = forms.CharField(label="Nombre", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    codigo_programa = forms.CharField(label="Código", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_inicio_programa = forms.DateTimeField(
        label="Fecha Inicio",
        widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    ESTADO_CHOICES = [
        ("Activo","Activo"),
        ("Inactivo","Inactivo")
    ]
    estado_programa = forms.ChoiceField(label = "Estado", choices= ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-control2'}))
    duracion_programa = forms.CharField(label="Duración", widget=forms.TextInput(attrs={'class': 'form-control'}))
    # facultad= forms.ModelChoiceField(label="Facultad", queryset=Facultad.objects.all(), help_text="Seleccione la facultad a la que pertenece el programa.")
    facultad_programa = forms.ModelChoiceField(label="Facultad", queryset=Facultad.objects.all(), widget=forms.Select(attrs={'class': 'form-control2'}))
    MODALIDADES_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
        ('Mixta', 'Mixta')
    ]
    modalidad_programa = forms.ChoiceField(label="Modalidad", choices=MODALIDADES_CHOICES, widget=forms.Select(attrs={'class': 'form-control2'}))

    def clean(self):
        cleaned_data = super().clean()

        # Get the selected faculty instance
        selected_faculty = cleaned_data.get('facultad_programa')

        # Validate the selected faculty
        if not selected_faculty:
            raise forms.ValidationError('Seleccione una facultad válida.')

        # Update the cleaned data with the faculty instance
        cleaned_data['facultad_programa'] = selected_faculty

        return cleaned_data



class ProgramacionAcademicaForm(forms.Form):
    programa_de_posgrado = forms.ModelChoiceField(label="Programa de posgrado", queryset= Programa_de_posgrado.objects.all(), help_text="Seleccione el programa")
    semestre = forms.ModelChoiceField(label="Semestre", queryset= Semestre.objects.all(), help_text="Seleccione el programa")
    departamento = forms.ModelChoiceField(label="Departamento", queryset= Departamento.objects.all(), help_text="Seleccione el departamento")
    num_creditos = forms.IntegerField(label = 'Numeros de creditos',help_text = "Escriba la cantidad de creditos totales que tendra el estudiante cuando curse esta programacion academica")
    horas = forms.FloatField(label='Horas totales', help_text= 'Escriba las horas totales de la materia')
    #periodo = forms.ModelChoiceField(label="Periodo", queryset= Periodo.objects.all(), help_text="Seleccione el periodo al que pertenece la programacion academica")
    materia = forms.ModelChoiceField(label="Materia", queryset= Materia.objects.all(), help_text="Seleccione las materias que desea asignar a la programacion academica")
    horario = forms.ModelChoiceField(label="Horario", queryset= Horario.objects.all(), help_text="Seleccione el horario de las materias que desea asignar a la programacion academica")

    def clean(self):
        cleaned_data = super().clean()

        # Get the selected faculty instance
        selected_programa = cleaned_data.get('programa_de_posgrado')
        selected_semestre = cleaned_data.get('semestre')
        selected_departamento = cleaned_data.get('departamento')
        selected_numcreditos = cleaned_data.get('num_creditos')
        selected_horas = cleaned_data.get('horas')
        selected_materia = cleaned_data.get('materia')
        selected_horario = cleaned_data.get('horario')


        selected = (selected_semestre,  selected_departamento, selected_programa, selected_numcreditos, selected_horas, selected_materia, selected_horario)

        # Validate the selected faculty
        if not selected:
            raise forms.ValidationError('Seleccione una opcion valida')

        # Update the cleaned data with the faculty instance
        cleaned_data['semestre'] = selected_semestre
        cleaned_data['departamento'] = selected_departamento
        cleaned_data['programa_de_posgrado'] = selected_programa
        cleaned_data['num_creditos'] = selected_numcreditos
        cleaned_data['horas'] = selected_horas
        cleaned_data['materia'] = selected_materia
        cleaned_data['horario'] = selected_horario

        return cleaned_data

class CrearMallaCurricular(forms.Form):
    nombre_malla = forms.CharField(label="Nombre", max_length=255)
    requisitos_previos = forms.CharField(label="Descripción", widget=forms.Textarea(), help_text="Ingrese una descripción de la malla curricular.")
    requisitos_previos = forms.CharField(label="Requisitos previos", widget=forms.Textarea(), help_text="Ingrese los requisitos previos a la malla curricular")
    programa_de_posgrado = forms.ModelChoiceField(label="Programa de posgrado", queryset=Programa_de_posgrado.objects.all(), help_text="Seleccione el programa de posgrado al que pertenece la malla.")

class CrearMateria(forms.Form):
    nombre_materia = forms.CharField(label="Nombre", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    codigo_materia = forms.CharField(label="Código", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    creditos_materia = forms.DecimalField(label="Creditos", max_digits=10, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    syllabus = forms.FileField(label='Selecciona un archivo', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    departamento = forms.CharField(label="Departamento", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class MateriaSearchForm(forms.Form):
    nombre_materia = forms.CharField(label='Nombre de la Materia', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
class MateriaEditForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre_materia', 'codigo_materia', 'creditos_materia', 'syllabus', 'departamento']
        widgets = {
            'nombre_materia': forms.TextInput(attrs={'class': 'form-control spaced-input'}),
            'codigo_materia': forms.TextInput(attrs={'class': 'form-control spaced-input'}),
            'syllabus': forms.FileInput(attrs={'class': 'form-control'}),
            'creditos_materia': forms.NumberInput(attrs={'class': 'form-control spaced-input'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control spaced-input'}),
        }

class RegistrarProfesor(forms.Form):
    nombre_profesor = forms.CharField(label="Nombre Completo", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cedula_profesor = forms.CharField(label="Identificación del profesor", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    especializacion_profesor = forms.CharField(label="Especialización", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo_electronico = forms.CharField(label="Correo", max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.IntegerField(label="Teléfono", widget=forms.NumberInput(attrs={'class': 'form-control'}))

class ProfesorSearchForm(forms.Form):
    nombre_profesor = forms.CharField(label='Nombre del Profesor', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class ProfesorEditForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre_profesor', 'cedula_profesor', 'especializacion_profesor', 'correo_electronico', 'telefono']
        widgets = {
            'nombre_profesor': forms.TextInput(attrs={'class': 'form-control spaced-input'}),
            'cedula_profesor': forms.TextInput(attrs={'class': 'form-control spaced-input'}),
            'especializacion_profesor': forms.TextInput(attrs={'class': 'form-control spaced-input'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control spaced-input'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control spaced-input'}),
        }
    
class BuscarProgramaForm(forms.Form):
    codigo = forms.CharField(label="Código del Programa", max_length=100)

class EditarProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa_de_posgrado
        fields = ['nombre_programa', 'codigo_programa', 'fecha_inicio_programa','estado_programa', 'duracion_programa', 'facultad_programa', 'modalidad_programa']
        widgets = {
            'estado': forms.Select(choices=Programa_de_posgrado.estado_programa),
        }

        
class DirectorDePrograma(forms.Form):
    nombre_director = forms.CharField(label = 'Nombre', max_length= 255)
    numero_director = forms.IntegerField(label = "Numero celular de contacto")
    correo_director = forms.CharField(label = "Correo Electronico", max_length= 500)
    foto_de_perfil = forms.ImageField()

class EspacioForm(forms.Form):
    espacio_codigo = forms.CharField(label = 'Nombre', max_length= 255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    capacidad_espacio = forms.IntegerField(label = "Capacidad", widget=forms.TextInput(attrs={'class': 'form-control'}))
    edificio_espacio = forms.ModelChoiceField(queryset=Edificio.objects.all(), label='Edificio', empty_label="Seleccione el edificio", widget=forms.Select(attrs={'class': 'form-control'}))
    DISPONIBILIDAD_CHOICES = [
        ("Disponible","Disponible"),
        ("No Disponible","No Disponible")
    ]
    disponibilidad_espacio = forms.ChoiceField(label="Disponibilidad", choices=DISPONIBILIDAD_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    TIPOS_CHOICES = (
        ('salon', 'salon'),
        ('auditorio', 'auditorio'),
        ('coliseo', 'coliseo'),
        ('sala computo', 'sala computo')
    )
    tipo = forms.ChoiceField(label="Modalidad", choices=TIPOS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
       
class CrearEdificio(forms.ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre_edificio', 'numero_espacios']
        labels = {
            'Nombre': 'nombre_edificio',
            'numero': 'numero_espacios',   
        }
        widgets = {
            'nombre_edificio': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_espacios': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
class EditarEspacio(forms.ModelForm):
    class Meta:
        model = Espacio
        fields = ['espacio_codigo', 'capacidad_espacio', 'edificio_espacio', 'disponibilidad_espacio', 'tipo']
        widgets = {
            'espacio_codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_espacio': forms.NumberInput(attrs={'class': 'form-control'}),
            'edificio_espacio': forms.Select(attrs={'class': 'form-control'}),
            'disponibilidad_espacio': forms.Select(choices=Espacio.disponibilidad_espacio, attrs={'class': 'form-control'}),
            'tipo': forms.Select(choices=Espacio.tipo, attrs={'class': 'form-control'})
        }

    

class EventoForm(forms.Form):
    nombre_evento = forms.CharField(label = 'Nombre', max_length= 255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_inicio_evento = forms.DateTimeField(
        label="Fecha Inicio",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
    )
    fecha_finalizacion_evento = forms.DateTimeField(
        label="Fecha Final",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
    )    
    lugar_evento = forms.ModelChoiceField(label="Lugar", queryset=Espacio.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion_evento = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'class': 'form-control'}))
    programa_de_posgrado_evento = forms.ModelChoiceField(label="Programa de Posgrado", queryset=Programa_de_posgrado.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    
class ActividadForm(forms.Form):
    nombre_actividad = forms.CharField(label = 'Nombre', max_length= 255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    duracion_en_horas = forms.IntegerField(label= "Duracion(Horas)", widget=forms.TextInput(attrs={'class': 'form-control'}))
    orador_actividad = forms.CharField(label = 'Encargado', max_length= 255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    evento_actividad = forms.ModelChoiceField(label="Evento", queryset=Evento.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
