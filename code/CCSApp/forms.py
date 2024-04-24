from django import forms
from .models import *


class RegistrarPeriodo(forms.Form):
    id_perido = forms.CharField(label = 'Id Periodo', max_length= 7, widget= forms.TextInput(attrs={'class': 'form-control'}))
    fecha_inicio_periodo = forms.DateField(label = "Fecha de inicio", widget = forms.DateTimeInput(attrs= {'type ' : 'date'}))
    fecha_final_periodo = forms.DateField(label = "Fecha de finalizacion", widget = forms.DateInput(attrs= {'type':'date'}))


class NewHorario(forms.Form):
    id_horario = forms.CharField(label= "Id", max_length =255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_inicio_hora = forms.DateTimeField(
        label="Fecha Inicio",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    fecha_final_hora = forms.DateTimeField(
        label="Fecha Final",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    
    
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
        ('mixta', 'Mixta'),
    ]
    modalidad = forms.ChoiceField(label="Modalidad", choices=MODALIDAD_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    enlace_virtual = forms.URLField(label="Enlace Virtual", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    espacio = forms.ModelChoiceField(label="Espacio", queryset=Espacio.objects.all(),empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    nrc = forms.ModelChoiceField(label="Nrc", queryset=Nrc.objects.all(),empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    
class ModificarHorarioForm(forms.Form):
    horario_id = forms.ModelChoiceField(queryset=Horario.objects.all(), label="Selecciona un horario para modificar", widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_inicio_hora = forms.DateTimeField(
        label="Fecha Inicio",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    fecha_final_hora = forms.DateTimeField(
        label="Fecha Final",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    nrc = forms.ModelChoiceField(label="Nrc", queryset=Nrc.objects.all(),empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
        ('mixta', 'Mixta'),
    ]
    modalidad = forms.ChoiceField(label="Nueva Modalidad", choices=MODALIDAD_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    enlace_virtual = forms.URLField(label="Nuevo Enlace Virtual", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    espacio = forms.CharField(label= "Espacio", max_length =255, widget=forms.Select(attrs={'class': 'form-control'}))

    

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
    password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class CrearProgramaAcademico(forms.Form):
    name = forms.CharField(label="Nombre", max_length=255, help_text="Ingrese el nombre del programa.")
    codigo = forms.CharField(label="Código", max_length=100, help_text="Ingrese el código del programa.")
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(), help_text="Ingrese una descripción del programa.")
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_finalizacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ESTADO_CHOICES = [
        ("Activo","Activo"),
        ("Inactivo","Inactivo")
    ]
    estado = forms.ChoiceField(label = "estado", choices= ESTADO_CHOICES, help_text= 'Seleccione el estado del programa' )
    duracion = forms.CharField(label="Duración", help_text="Ingrese la duración del programa.")
    facultad= forms.ModelChoiceField(label="Facultad", queryset=Facultad.objects.all(), help_text="Seleccione la facultad a la que pertenece el programa.")
    MODALIDADES_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
        ('Mixta', 'Mixta')
    ]
    modalidad = forms.ChoiceField(label="Modalidad", choices=MODALIDADES_CHOICES, help_text="Seleccione la modalidad del programa.")

class CrearMallaCurricular(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=255)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(), help_text="Ingrese una descripción de la malla curricular.")
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
    nombre_profesor = forms.CharField(label="Nombre", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cedula_profesor = forms.CharField(label="Identificación del profesor", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    especializacion_profesor = forms.CharField(label="Especialización", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo_electronico = forms.CharField(label="Correo", max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.IntegerField(label="Teléfono", widget=forms.NumberInput(attrs={'class': 'form-control'}))

class ProfesorSearchForm(forms.Form):
    nombre_profesor = forms.CharField(label='Nombre del Profesor', max_length=255)

class ProfesorEditForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre_profesor', 'cedula_profesor', 'especializacion_profesor', 'correo_electronico', 'telefono']
    
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
    nombre = forms.CharField(label = 'Nombre', max_length= 255)
    numero = forms.IntegerField(label = "Numero celular de contacto")
    correo = forms.CharField(label = "Correo Electronico", max_length= 500)
    descripcion_cargo = forms.CharField(label= "Descripcion", widget= forms.Textarea())
    foto_de_perfil = forms.ImageField

class ProgramacionSemestral(forms.Form):    
    Programa = forms.ModelChoiceField(queryset= Programa_de_posgrado.objects.all(), label='Programa', empty_label="Seleccione un programa")
    
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
    
class EditarEspacio(forms.ModelForm):
    class Meta:
        model = Espacio
        fields = ['espacio_codigo', 'capacidad_espacio', 'edificio_espacio', 'disponibilidad_espacio', 'tipo']
        widgets = {
            'disponibilidad_espacio': forms.Select(choices=Espacio.disponibilidad_espacio),
            'tipo': forms.Select(choices=Espacio.tipo)
        }