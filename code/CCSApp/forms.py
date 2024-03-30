from django import forms
from .models import *

class NewHorario(forms.Form):
    fecha_hora = forms.DateTimeField(label="Fecha y Hora", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    profesor = forms.CharField(label="Profesor", max_length=100)
    materia = forms.CharField(label="Materia", max_length=255)
    
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
        ('mixta', 'Mixta'),
    ]
    modalidad = forms.ChoiceField(label="Modalidad", choices=MODALIDAD_CHOICES)
    enlace_virtual = forms.URLField(label="Enlace Virtual", required=False)
    salon_presencial = forms.CharField(label="Salon Presencial", max_length=50, required=False)
    
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
    fecha_inicio = forms.DateField(label="Fecha de inicio", help_text="Ingrese la fecha de inicio del programa.")
    fecha_finalizacion = forms.DateField(label="Fecha de finalización", help_text="Ingrese la fecha de finalización del programa.")
    value = forms.DecimalField(label="Valor", max_digits=10, help_text="Ingrese el valor del programa.")
    duracion = forms.CharField(label="Duración", help_text="Ingrese la duración del programa.")
    facultad= forms.ModelChoiceField(label="Facultad", queryset=Facultad.objects.all(), help_text="Seleccione la facultad a la que pertenece el programa.")
    MODALIDADES_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
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

    