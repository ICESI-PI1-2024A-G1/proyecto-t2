from django import forms
from .forms import *
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
            raise forms.ValidationError("El profesor seleccionado no está registrado, intente nuevamente.")
        return profesor_nombre

    def clean_materia(self):
        materia_nombre = self.cleaned_data.get('materia')
        if not Materia.objects.filter(nombre=materia_nombre).exists():
            raise forms.ValidationError("La materia seleccionada no está registrada, intente nuevamente.")
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
    
class ModificarHorarioForm(forms.Form):
    fecha_hora = forms.DateTimeField(label="Fecha y Hora", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    profesor = forms.CharField(label="Profesor", max_length=100)
    
    # Campo de búsqueda para seleccionar la materia existente
    materia = forms.ModelChoiceField(label="Materia", queryset=Materia.objects.all())
    
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
            raise forms.ValidationError("El profesor seleccionado no está registrado, intente nuevamente.")
        return profesor_nombre

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