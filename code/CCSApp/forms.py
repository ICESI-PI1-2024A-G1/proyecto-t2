from django import forms

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
    nombre = forms.CharField(label="Nombre de usuario", max_length=150)
    codigo = forms.CharField(label="Código", max_length=100, widget=forms.PasswordInput)

class CrearProgramaAcademico(forms.Form):
    name = forms.CharField(label="Nombre", max_length=255)
    codigo = forms.CharField(label="Código", max_length=100)
    descripcion = forms.CharField(label="Descripción", widget=forms.TextInput())
    fecha_inicio = forms.DateField(label="Fecha de inicio")
    fecha_finalizacion = forms.DateField(label="Fecha de finalización")
    value = forms.DecimalField(label="Valor", max_digits=10)
    duracion = forms.CharField(label="Duración")
    facultad= forms.CharField(label="facultad")
    MODALIDADES_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
    ]
    modalidad = forms.ChoiceField(label="Modalidad", choices=MODALIDADES_CHOICES)
