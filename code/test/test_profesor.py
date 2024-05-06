import pytest

from CCSApp.models import Profesor
from django.test import TestCase
from CCSApp.forms import ProfesorSearchForm, ProfesorEditForm

@pytest.mark.django_db
def test_usuario_creation():
    usuario = Profesor.objects.create(
        nombre_profesor = 'Fernando Mejia',
        cedula_profesor = '123456789',
        especializacion_profesor = 'DoctoradoMates',
        correo_electronico = 'fernandom@gmail.com',
        telefono = 32141643,
        
    )
    assert usuario.cedula_profesor == '123456789'
    


class TestProfesorSearchForm(TestCase):
    def test_valid_form(self):
        # Creamos datos válidos para el formulario
        form_data = {'nombre_profesor': 'Juan Pérez'}
        form = ProfesorSearchForm(data=form_data)

        # Verificamos que el formulario sea válido
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Creamos datos inválidos para el formulario
        form_data = {'nombre_profesor': ''}
        form = ProfesorSearchForm(data=form_data)

        # Verificamos que el formulario sea inválido
        self.assertFalse(form.is_valid())
        

class TestProfesorEditForm(TestCase):
    def setUp(self):
        self.profesor = Profesor.objects.create(
            nombre_profesor='Juan Pérez',
            cedula_profesor='1234567890',
            especializacion_profesor='Ingeniería de Software',
            correo_electronico='juan@example.com',
            telefono='123456789'
        )

    def test_valid_form(self):
        # Creamos datos válidos para el formulario
        form_data = {
            'nombre_profesor': 'Juan Pérez',
            'cedula_profesor': '1234567890',
            'especializacion_profesor': 'Ciencias de la Computación',
            'correo_electronico': 'juan@example.com',
            'telefono': '987654321'
        }
        form = ProfesorEditForm(data=form_data, instance=self.profesor)

        # Verificamos que el formulario sea válido
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Creamos datos inválidos para el formulario
        form_data = {
            'nombre_profesor': 'Juan Pérez',
            'cedula_profesor': '1234567890',
            'especializacion_profesor': '',
            'correo_electronico': 'juan@example.com',
            'telefono': ''
        }
        form = ProfesorEditForm(data=form_data, instance=self.profesor)

        # Verificamos que el formulario sea inválido
        self.assertFalse(form.is_valid())
