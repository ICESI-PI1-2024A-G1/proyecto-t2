from django import forms
from .models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['fecha_hora', 'profesor', 'materia', 'modalidad', 'enlace_virtual', 'salon_presencial']
