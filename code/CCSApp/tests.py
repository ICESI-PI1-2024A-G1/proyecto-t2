from django.test import TestCase
from .models import *
from .forms import *

class NewHorarioFormTests(TestCase):

    def test_invalid_modalidad(self):
        # Prueba con modalidad inválida
        form_data = {
            'fecha_hora': '2024-03-17T12:00',
            'profesor': 'Juan Perez',
            'materia': '445688',
            'modalidad': 'invalida',  # Modalidad no válida
            'salon_presencial': '201C',
        }
        form = NewHorario(data=form_data)
        self.assertFalse(form.is_valid())  # Debe ser inválido debido a la modalidad

    def test_empty_data(self):
        # Prueba con datos vacíos
        form = NewHorario(data={})
        self.assertFalse(form.is_valid())  # Debe ser inválido debido a campos requeridos
