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
    duracion = forms.CharField(label="Duración", help_text="Ingrese la duración del programa.")
    facultad= forms.ModelChoiceField(label="Facultad", queryset=Facultad.objects.all(), help_text="Seleccione la facultad a la que pertenece el programa.")
    MODALIDADES_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
        ('Mixta', 'Mixta')
    ]
    modalidad = forms.ChoiceField(label="Modalidad", choices=MODALIDADES_CHOICES, help_text="Seleccione la modalidad del programa.")

class MallaCurricularForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=255)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea())
    requisitos_previos = forms.CharField(label="Requisitos Previos", widget=forms.Textarea())
    programa_de_posgrado = forms.ModelChoiceField(label="Programa de Posgrado", queryset=Programa_de_posgrado.objects.all())

class DirectorDePrograma(forms.Form):
    nombre = forms.CharField(label = 'Nombre', max_length= 255)
    numero = forms.IntegerField(label = "Numero celular de contacto")
    correo = forms.CharField(label = "Correo Electronico", max_length= 500)
    descripcion_cargo = forms.CharField(label= "Descripcion", widget= forms.Textarea())
    foto_de_perfil = forms.ImageField()