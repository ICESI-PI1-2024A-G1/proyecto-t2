from django import forms
from .models import *

class NewHorario(forms.Form):
    fecha_hora = forms.DateTimeField(label="Fecha y Hora", widget=forms.DateTimeInput(attrs={'type': 'date'}))
    profesor = forms.CharField(label="Profesor", max_length=100)
    materia = forms.CharField(label="Materia", max_length=255)
    
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
        ('mixta', 'Mixta'),
    ]
    modalidad = forms.ChoiceField(label="Modalidad", choices=MODALIDAD_CHOICES)
    enlace_virtual = forms.URLField(label="Enlace Virtual", required=False)
    espacio = forms.CharField(label="Salon Presencial", max_length=50, required=False)
    
    def clean_profesor(self):
        profesor_nombre = self.cleaned_data.get('profesor')
        if not Profesor.objects.filter(nombre=profesor_nombre).exists():
            raise forms.ValidationError("El profesor seleccionado no está registrado.")
        return profesor_nombre

    def clean_materia(self):
        materia_nombre = self.cleaned_data.get('materia')
        if not Materia.objects.filter(nombre=materia_nombre).exists():
            raise forms.ValidationError("La materia seleccionada no está registrada.")
        return materia_nombre
    
    def clean_espacio(self):
        espacio_nombre = self.cleaned_data.get('espacio')
        if not Materia.objects.filter(nombre=espacio_nombre).exists():
            raise forms.ValidationError("El espacio seleccionada no está registrada.")
        return espacio_nombre
    

    def clean(self):
        cleaned_data = super().clean()
        modalidad = cleaned_data.get('modalidad')
        salon_presencial = cleaned_data.get('salon_presencial')
        enlace_virtual = cleaned_data.get('enlace_virtual')

        if modalidad == 'presencial' and not salon_presencial:
            raise forms.ValidationError("Debe proporcionar un salón para la modalidad presencial.")
        elif modalidad == 'mixta' and (not salon_presencial or not enlace_virtual):
            raise forms.ValidationError("Debe proporcionar un salón y un enlace virtual para la modalidad mixta.")
        elif modalidad == 'virtual' and not enlace_virtual:
            raise forms.ValidationError("Debe proporcionar un enlace virtual para la modalidad virtual.")

        return cleaned_data
    
class ModificarHorarioForm(forms.Form):
    horario_id = forms.ModelChoiceField(queryset=Horario.objects.all(), label="Selecciona un horario para modificar")
    fecha_hora = forms.DateTimeField(label="Nueva Fecha y Hora", widget=forms.DateTimeInput(attrs={'type': 'date'}))
    profesor = forms.CharField(label="Nuevo Profesor", max_length=100)
    materia = forms.CharField(label="Nueva Materia", max_length=255)
    
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
        ('mixta', 'Mixta'),
    ]
    modalidad = forms.ChoiceField(label="Nueva Modalidad", choices=MODALIDAD_CHOICES)
    enlace_virtual = forms.URLField(label="Nuevo Enlace Virtual", required=False)
    salon_presencial = forms.CharField(label="Nuevo Salon Presencial", max_length=50, required=False)

class NewUsuary(forms.Form):
    nombre = forms.CharField(label= "nombre", max_length =255)
    codigo = forms.CharField(label= "codigo", max_length = 100)
    rol = forms.CharField(label= "rol", max_length=255)
    departamento = forms.CharField(label= "departamento", max_length=500)
    correo_electronico = forms.EmailField(label="correo electronico", max_length=500)
    telefono = forms.IntegerField(label= "telefono")

class LoginForm(forms.Form):
    codigo = forms.CharField(max_length=10)
    correo_electronico = forms.EmailField()

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
    nombre = forms.CharField(label="Nombre", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    codigo = forms.CharField(label="Código", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'class': 'form-control'}))
    creditos = forms.DecimalField(label="Creditos", max_digits=10, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    syllabus = forms.CharField(label="Syllabus", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class RegistrarProfesor(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    codigo = forms.CharField(label="Identificación del profesor", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    especializacion = forms.CharField(label="Especialización", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo = forms.CharField(label="Correo", max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.IntegerField(label="Teléfono", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    materias = forms.ModelChoiceField(label="Materia Asignada", queryset=Materia.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

    
    nombre = forms.CharField(label="Nombre", max_length=255)
    codigo = forms.CharField(label="Código", max_length=100, help_text="Ingrese el código de la materia.")    
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(), help_text="Ingrese una descripción de la materia")
    creditos = forms.DecimalField(label="Creditos", max_digits=10, help_text="Ingrese el numero de creditos")
    syllabus = forms.CharField(label="Syllabus", max_length=255)
    
class BuscarProgramaForm(forms.Form):
    codigo = forms.CharField(label="Código del Programa", max_length=100)

class EditarProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa_de_posgrado
        fields = ['name', 'codigo', 'descripcion', 'fecha_inicio', 'fecha_finalizacion','estado', 'duracion', 'facultad', 'modalidad']
        widgets = {
            'estado': forms.Select(choices=Programa_de_posgrado.estado),
        }

        
class DirectorDePrograma(forms.Form):
    nombre = forms.CharField(label = 'Nombre', max_length= 255)
    numero = forms.IntegerField(label = "Numero celular de contacto")
    correo = forms.CharField(label = "Correo Electronico", max_length= 500)
    descripcion_cargo = forms.CharField(label= "Descripcion", widget= forms.Textarea())
    foto_de_perfil = forms.ImageField()

class ProgramacionSemestral(forms.Form):    
    Programa = forms.ModelChoiceField(queryset= Programa_de_posgrado.objects.all(), label='Programa', empty_label="Seleccione un programa")
    
class EspacioForm(forms.ModelForm):
    class Meta:
        model = Espacio
        fields = ['nombre', 'ubicacion', 'capacidad', 'disponibilidad', 'tipo']
        labels = {
            'nombre': 'Nombre',
            'ubicacion': 'Ubicación',
            'capacidad': 'Capacidad',
            'disponibilidad': 'Disponibilidad',
            'tipo': 'Tipo',
        }
        widgets = {
            'disponibilidad': forms.Select(choices=[('Disponible', 'Disponible'), ('No Disponible', 'No Disponible')]),
            'tipo': forms.Select(choices=[
                ('salon', 'Salón'),
                ('auditorio', 'Auditorio'),
                ('coliseo', 'Coliseo'),
                ('sala_computo', 'Sala de Computo')
            ])
        }
