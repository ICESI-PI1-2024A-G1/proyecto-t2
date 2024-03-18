from django import forms

class NewUsuary(forms.Form):
    nombre = forms.CharField(label= "nombre", max_length =255)
    codigo = forms.CharField(label= "codigo", max_length = 100)
    rol = forms.CharField(label= "rol", max_length=255)
    departamento = forms.CharField(label= "departamento", max_length=500)
    correo_electronico = forms.CharField(label= "correo electronico", max_length=500)
    telefono = forms.IntegerField(label= "telefono")

class CrearProgramaAcademico(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=255)
    codigo = forms.CharField(label="Código", max_length=100)
    descripcion = forms.CharField(label="Descripción", widget=forms.TextInput())
    fecha_inicio = forms.DateField(label="Fecha de inicio")
    fecha_finalizacion = forms.DateField(label="Fecha de finalización")
    value = forms.DecimalField(label="Valor", max_digits=10)
    duracion = forms.DecimalField(label="Duración")
    MODALIDADES_CHOICES = [
        ('diurna', 'Diurna'),
        ('nocturna', 'Nocturna'),
    ]
    modalidad = forms.ChoiceField(label="Modalidad", choices=MODALIDADES_CHOICES)