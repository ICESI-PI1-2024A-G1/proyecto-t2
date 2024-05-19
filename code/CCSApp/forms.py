from django import forms
from .models import *


class RegistrarPeriodo(forms.Form):
    id_perido = forms.CharField(label = 'Id Periodo', max_length= 7, widget= forms.TextInput(attrs={'class': 'form-control'}))
    fecha_inicio_periodo = forms.DateField(label = "Fecha de inicio", widget = forms.DateTimeInput(attrs= {'type ' : 'date'}))
    fecha_final_periodo = forms.DateField(label = "Fecha de finalizacion", widget = forms.DateInput(attrs= {'type':'date'}))


class NewHorario(forms.Form):
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
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
        ('Mixta', 'Mixta'),
    ]

    GRUPO = [
        ('001', '001'),
        ('002', '002'),
        ('003', '003'),
        ('004', '004')
    ]
    modalidad = forms.ChoiceField(label="Modalidad", choices=MODALIDAD_CHOICES, widget=forms.Select(attrs={'class': 'form-control2'}))
    enlace_virtual = forms.URLField(label="Enlace Virtual", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    salon_presencial = forms.ModelChoiceField(label="Espacio", queryset=Espacio.objects.all(),empty_label=None, widget=forms.Select(attrs={'class': 'form-control2'}))
    materia = forms.ModelChoiceField(label="Materia", queryset=Materia.objects.all(),empty_label=None, widget=forms.Select(attrs={'class': 'form-control2'}))
    grupo = forms.ChoiceField(label="Grupo", choices=GRUPO, widget=forms.Select(attrs={'class': 'form-control2'}))

    def clean(self):
        cleaned_data = super().clean()
        modalidad = cleaned_data.get('modalidad')
        enlace_virtual = cleaned_data.get('enlace_virtual')

        if modalidad == 'Virtual' and not enlace_virtual:
            self.add_error('enlace_virtual', 'Este campo es obligatorio cuando la modalidad es Virtual.')

        return cleaned_data
    
class ModificarHorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['fecha_inicio_horario', 'hora_inicio_horario', 'hora_final_horario', 'materia', 'modalidad', 'grupo', 'enlace_virtual', 'salon_presencial']
        widgets = {
            'fecha_inicio_horario': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_inicio_horario': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hora_final_horario': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'materia': forms.TextInput(attrs={'class': 'form-control2', 'readonly': 'readonly', 'style': 'background-color: #d3d3d3'}),
            'modalidad': forms.Select(attrs={'class': 'form-control2'}),
            'grupo': forms.Select(attrs={'class': 'form-control2'}),
            'enlace_virtual': forms.TextInput(attrs={'class': 'form-control'}),
            'salon_presencial': forms.Select(attrs={'class': 'form-control2'}),
        }

    def __init__(self, *args, **kwargs):
        super(ModificarHorarioForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['materia'].widget.attrs['value'] = self.instance.materia.nombre_materia

    def clean(self):
        cleaned_data = super().clean()
        modalidad = cleaned_data.get('modalidad')
        enlace_virtual = cleaned_data.get('enlace_virtual')

        if modalidad == 'Virtual' and not enlace_virtual:
            self.add_error('enlace_virtual', 'Este campo es obligatorio cuando la modalidad es Virtual.')

        return cleaned_data

class NewUsuary(forms.Form):
    nombre = forms.CharField(label= "Nombre", max_length =255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cedula = forms.CharField(label= "Cédula", max_length = 100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rol = forms.CharField(label= "Rol", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    departamento = forms.CharField(label= "Departamento", max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo_electronico = forms.EmailField(label="Correo Electronico", max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(label= "Telefono", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

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
    duracion_programa = forms.CharField(label="Duración en Años", widget=forms.TextInput(attrs={'class': 'form-control'}))
    # facultad= forms.ModelChoiceField(label="Facultad", queryset=Facultad.objects.all(), help_text="Seleccione la facultad a la que pertenece el programa.")
    facultad_programa = forms.ModelChoiceField(label="Facultad", queryset=Facultad.objects.all(), widget=forms.Select(attrs={'class': 'form-control2'}))
    MODALIDADES_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
        ('Mixta', 'Mixta')
    ]
    modalidad_programa = forms.ChoiceField(label="Modalidad", choices=MODALIDADES_CHOICES, widget=forms.Select(attrs={'class': 'form-control2'}))
    director_programa= forms.ModelChoiceField(label="Director De Programa", queryset=Director_de_programa.objects.all(), widget=forms.Select(attrs={'class': 'form-control2'}))    

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

from django import forms
from .models import Programa_de_posgrado, Semestre, Departamento, Materia, Horario, Profesor

class ProgramacionAcademicaForm(forms.Form):
    programa_de_posgrado = forms.ModelChoiceField(
        label="Programa de posgrado",
        queryset=Programa_de_posgrado.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control2', 'id': 'id_programa_de_posgrado'})
    )
    semestre = forms.ModelChoiceField(
        label="Semestre",
        queryset=Semestre.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control2', 'id': 'id_semestre'})
    )
    departamento = forms.ModelChoiceField(
        label="Departamento",
        queryset=Departamento.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control2'})
    )
    materia = forms.ModelChoiceField(
        label="Materia",
        queryset=Materia.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control2', 'id': 'id_materia'})
    )
    horario = forms.ModelChoiceField(
        label="Horarios",
        queryset=Horario.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control2', 'id': 'id_horario'})
    )
    periodo = forms.ModelChoiceField(
        label="Periodo",
        queryset=Periodo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control2', 'id': 'id_periodo'})
    )
    horas = forms.FloatField(
        label='Horas Totales',
        widget=forms.NumberInput(attrs={'class': 'form-control2', 'id': 'id_horas'})
    )
    grupo = forms.ChoiceField(
        choices=[('001', '001'), ('002', '002'), ('003', '003'), ('004', '004')],
        label="Grupo",
        widget=forms.HiddenInput(),
        required=False
    )
    profesor = forms.ModelChoiceField(
        label="Profesor",
        queryset=Profesor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control2'})
    )
    num_creditos = forms.IntegerField(
        label='Número de Créditos',
        widget=forms.HiddenInput(),
        required=False
    )
    modalidad = forms.CharField(
        label='Modalidad',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='Presencial'  # Puedes definir un valor por defecto si es necesario
    )
    tipo_de_contrato = forms.CharField(
        label='Tipo de Contrato',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='N/A'  # Puedes definir un valor por defecto si es necesario
    )
    ciudad = forms.CharField(
        label='Ciudad',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='Cali'  # Puedes definir un valor por defecto si es necesario
    )
    correo_electronico = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='correo@ejemplo.com'  # Puedes definir un valor por defecto si es necesario
    )
    telefono = forms.CharField(
        label='Teléfono',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='123456789'  # Puedes definir un valor por defecto si es necesario
    )
    fecha_de_clase = forms.DateField(
        label='Fecha de Clase',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='2023-01-01'  # Puedes definir un valor por defecto si es necesario
    )
    estado_de_contrato = forms.CharField(
        label='Estado de Contrato',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='Activo'  # Puedes definir un valor por defecto si es necesario
    )
    fecha_elab_contrato = forms.CharField(
        label='Fecha Elaboración de Contrato',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='N/A'  # Puedes definir un valor por defecto si es necesario
    )
    num_contrato = forms.CharField(
        label='Número de Contrato',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='N/A'  # Puedes definir un valor por defecto si es necesario
    )
    listas_mosaicos = forms.CharField(
        label='Listas y Mosaicos',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='N/A'  # Puedes definir un valor por defecto si es necesario
    )
    entrega_notas = forms.CharField(
        label='Entrega de Notas',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='N/A'  # Puedes definir un valor por defecto si es necesario
    )
    intu_canvas = forms.CharField(
        label='Intu Canvas',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='N/A'  # Puedes definir un valor por defecto si es necesario
    )
    tiquetes = forms.CharField(
        label='Tiquetes',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='N/A'  # Puedes definir un valor por defecto si es necesario
    )
    hotel = forms.CharField(
        label='Hotel',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='N/A'  # Puedes definir un valor por defecto si es necesario
    )
    viaticos = forms.CharField(
        label='Viáticos',
        widget=forms.HiddenInput(),  # Campo oculto
        initial='N/A'  # Puedes definir un valor por defecto si es necesario
    )

    def clean(self):
        cleaned_data = super().clean()

        # Obtener las instancias seleccionadas
        selected_programa = cleaned_data.get('programa_de_posgrado')
        selected_semestre = cleaned_data.get('semestre')
        selected_departamento = cleaned_data.get('departamento')
        selected_materia = cleaned_data.get('materia')
        selected_horario = cleaned_data.get('horario')
        selected_profesor = cleaned_data.get('profesor')
        selected_horas = cleaned_data.get('horas')

        # Validar las opciones seleccionadas
        if not all([selected_programa, selected_semestre, selected_departamento, selected_materia, selected_horario, selected_profesor, selected_horas]):
            raise forms.ValidationError('Seleccione una opción válida en todos los campos.')

        # Obtener el número de créditos de la materia seleccionada
        if selected_materia:
            cleaned_data['num_creditos'] = selected_materia.creditos_materia

        if selected_horario:
            cleaned_data['modalidad'] = selected_horario.modalidad
            cleaned_data['fecha_de_clase'] = selected_horario.fecha_inicio_horario
            cleaned_data['grupo'] = selected_horario.grupo

        if selected_profesor:
            cleaned_data['correo_electronico'] = selected_profesor.correo_electronico
            cleaned_data['telefono'] = selected_profesor.telefono
            cleaned_data['tipo_de_contrato'] = selected_profesor.cedula_profesor

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
    departamento = forms.ModelChoiceField(label="Departamento", queryset= Departamento.objects.all(), widget=forms.Select(attrs={'class': 'form-control2'}))
    semestre = forms.ModelChoiceField(label="Semestre", queryset= Semestre.objects.all(), widget=forms.Select(attrs={'class': 'form-control2'}))
    programa_de_posgrado_materia = forms.ModelChoiceField(label="Programa de posgrado", queryset= Programa_de_posgrado.objects.all(), widget=forms.Select(attrs={'class': 'form-control2'}))

class MateriaSearchForm(forms.Form):
    nombre_materia = forms.CharField(label='Nombre de la Materia', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
class MateriaEditForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre_materia', 'codigo_materia', 'creditos_materia', 'syllabus', 'departamento', 'semestre']
        widgets = {
            'nombre_materia': forms.TextInput(attrs={'class': 'form-control spaced-input', 'readonly': 'readonly', 'style': 'background-color: #d3d3d3'}),
            'codigo_materia': forms.TextInput(attrs={'class': 'form-control spaced-input', 'readonly': 'readonly', 'style': 'background-color: #d3d3d3'}),
            'syllabus': forms.FileInput(attrs={'class': 'form-control'}),
            'creditos_materia': forms.NumberInput(attrs={'class': 'form-control spaced-input'}),
            'departamento': forms.Select(attrs={'class': 'form-control2'}),
            'semestre' : forms.Select(attrs={'class': 'form-control2'}),
        }

class RegistrarProfesor(forms.Form):
    nombre_profesor = forms.CharField(label="Nombre Completo", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cedula_profesor = forms.CharField(label="Identificación del profesor", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    especializacion_profesor = forms.CharField(label="Especialización", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo_electronico = forms.CharField(label="Correo", max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(label="Teléfono", widget=forms.TextInput(attrs={'class': 'form-control'}))

class ProfesorSearchForm(forms.Form):
    nombre_profesor = forms.CharField(label='Nombre del Profesor', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class ProfesorEditForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre_profesor', 'cedula_profesor', 'especializacion_profesor', 'correo_electronico', 'telefono']
        widgets = {
            'nombre_profesor': forms.TextInput(attrs={'class': 'form-control spaced-input',  'readonly': 'readonly', 'style': 'background-color: #d3d3d3'}),
            'cedula_profesor': forms.TextInput(attrs={'class': 'form-control spaced-input','readonly': 'readonly', 'style': 'background-color: #d3d3d3'}),
            'especializacion_profesor': forms.TextInput(attrs={'class': 'form-control spaced-input'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control spaced-input'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control spaced-input'}),
        }
    
class BuscarProgramaForm(forms.Form):
    codigo_programa = forms.CharField(label="Código del Programa", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class EditarProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa_de_posgrado
        fields = ['nombre_programa', 'codigo_programa', 'fecha_inicio_programa','estado_programa', 'duracion_programa', 'facultad_programa', 'modalidad_programa', 'director_programa']
        widgets = {
            'nombre_programa': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_programa': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'style': 'background-color: #d3d3d3'}),
            'fecha_inicio_programa': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'duracion_programa': forms.TextInput(attrs={'class': 'form-control'}),
            'facultad_programa': forms.Select(attrs={'class': 'form-control'}),
            'modalidad_programa': forms.Select(attrs={'class': 'form-control'}),
            'estado_programa': forms.Select(attrs={'class': 'form-control'}),
            'director_programa' : forms.Select(attrs={'class': 'form-control'})
        }

        
class DirectorDePrograma(forms.Form):
    nombre_director = forms.CharField(label = 'Nombre', max_length= 255)
    numero_director = forms.CharField(label = "Numero celular de contacto")
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
        ('salon', 'Salon'),
        ('auditorio', 'Auditorio'),
        ('coliseo', 'Coliseo'),
        ('sala computo', 'Sala de Computo')
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
            'espacio_codigo': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'style': 'background-color: #d3d3d3'}),
            'capacidad_espacio': forms.NumberInput(attrs={'class': 'form-control'}),
            'edificio_espacio': forms.Select(attrs={'class': 'form-control'}),
            'disponibilidad_espacio': forms.Select(choices=Espacio.disponibilidad_espacio, attrs={'class': 'form-control'}),
            'tipo': forms.Select(choices=Espacio.tipo, attrs={'class': 'form-control'})
        }

    

class EventoForm(forms.Form):
    nombre_evento = forms.CharField(label = 'Nombre', max_length= 255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_inicio_evento = forms.DateTimeField(
        label="Fecha Inicio",
        widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    fecha_finalizacion_evento = forms.DateTimeField(
        label="Fecha Final",
        widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),
    )    
    lugar_evento = forms.ModelChoiceField(label="Lugar", queryset=Espacio.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion_evento = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'class': 'form-control'}))
    programa_de_posgrado_evento = forms.ModelChoiceField(label="Programa de Posgrado", queryset=Programa_de_posgrado.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    
class ActividadForm(forms.Form):
    nombre_actividad = forms.CharField(label = 'Nombre', max_length= 255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    duracion_en_horas = forms.IntegerField(label= "Duracion(Horas)", widget=forms.TextInput(attrs={'class': 'form-control'}))
    orador_actividad = forms.CharField(label = 'Encargado', max_length= 255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    evento_actividad = forms.ModelChoiceField(label="Evento", queryset=Evento.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

class ProgramacionAcademicaEditForm(forms.ModelForm):
    class Meta:
        model = ProgramacionAcademica
        fields = [
            'programa_de_posgrado', 'semestre', 'departamento', 'materia', 
            'horario', 'periodo', 'horas', 'grupo', 'docente', 'num_creditos', 
            'modalidad', 'tipo_de_contrato', 'ciudad', 'correo_electronico', 
            'telefono', 'fecha_de_clase', 'estado_de_contrato', 
            'fecha_elab_contrato', 'num_contrato', 'listas_mosaicos', 
            'entrega_notas', 'intu_canvas', 'tiquetes', 'hotel', 'viaticos'
        ]
        widgets = {
            'programa_de_posgrado': forms.Select(attrs={'class': 'form-control2', 'id': 'id_programa_de_posgrado'}),
            'semestre': forms.Select(attrs={'class': 'form-control2', 'id': 'id_semestre'}),
            'departamento': forms.Select(attrs={'class': 'form-control2'}),
            'materia': forms.Select(attrs={'class': 'form-control2', 'id': 'id_materia'}),
            'horario': forms.Select(attrs={'class': 'form-control2', 'id': 'id_horario'}),
            'periodo': forms.Select(attrs={'class': 'form-control2', 'id': 'id_periodo'}),
            'horas': forms.NumberInput(attrs={'class': 'form-control2', 'id': 'id_horas'}),
            'grupo': forms.HiddenInput(),
            'docente': forms.Select(attrs={'class': 'form-control2'}),
            'num_creditos': forms.HiddenInput(),
            'modalidad': forms.HiddenInput(),
            'tipo_de_contrato': forms.HiddenInput(),
            'ciudad': forms.HiddenInput(),
            'correo_electronico': forms.HiddenInput(),
            'telefono': forms.HiddenInput(),
            'fecha_de_clase': forms.HiddenInput(),
            'estado_de_contrato': forms.HiddenInput(),
            'fecha_elab_contrato': forms.HiddenInput(),
            'num_contrato': forms.HiddenInput(),
            'listas_mosaicos': forms.HiddenInput(),
            'entrega_notas': forms.HiddenInput(),
            'intu_canvas': forms.HiddenInput(),
            'tiquetes': forms.HiddenInput(),
            'hotel': forms.HiddenInput(),
            'viaticos': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        # Validaciones personalizadas aquí si es necesario
        return cleaned_data