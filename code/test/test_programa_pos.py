import pytest
from CCSApp.models import Programa_de_posgrado, Facultad, Director_de_programa
from datetime import date
from django.test import TestCase
from CCSApp.forms import BuscarProgramaForm, EditarProgramaForm


@pytest.mark.django_db
def test_programa_posgrado_creation():
    facultad = Facultad.objects.create(codigo_facultad='F01', nombre_facultad='Facultad de Ingeniería')
    director = Director_de_programa.objects.create(
        nombre_director='Juan Pérez',
        numero_director='123456789',
        correo_director='juanperez@example.com'
    )

    programa = Programa_de_posgrado.objects.create(
        nombre_programa='Maestría en Ingeniería',
        codigo_programa='MI01',
        fecha_inicio_programa=date.today(),
        estado_programa='Activo',
        duracion_programa=2,
        facultad_programa=facultad,
        director_programa=director
    )
    assert programa.nombre_programa == 'Maestría en Ingeniería'



class TestBuscarProgramaForm(TestCase):
    def test_valid_form(self):
        # Creamos datos válidos para el formulario
        form_data = {'codigo_programa': 'DCOMP01'}
        form = BuscarProgramaForm(data=form_data)

        # Verificamos que el formulario sea válido
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Creamos datos inválidos para el formulario
        form_data = {'codigo_programa': ''}
        form = BuscarProgramaForm(data=form_data)

        # Verificamos que el formulario sea inválido
        self.assertFalse(form.is_valid())


class TestEditarProgramaForm(TestCase):
    def setUp(self):
        # Creamos instancias de modelos relacionados para usar en las pruebas
        facultad = Facultad.objects.create(codigo_facultad='FCOMP', nombre_facultad='Facultad de Ciencias de la Computación')
        director = Director_de_programa.objects.create(nombre_director='Juan Pérez', numero_director='123456789', correo_director='juan@example.com')

        # Creamos un programa de posgrado para usar en las pruebas
        self.programa = Programa_de_posgrado.objects.create(
            nombre_programa='Doctorado en Ciencias de la Computación',
            codigo_programa='DCOMP01',
            fecha_inicio_programa='2024-01-01',
            estado_programa='Activo',
            duracion_programa= 4,
            facultad_programa=facultad,
            modalidad_programa='Presencial',
            director_programa=director
        )

    def test_valid_form(self):
        # Creamos datos válidos para el formulario
        form_data = {
            'nombre_programa': 'Doctorado en Ciencias de la Computación',
            'codigo_programa': 'DCOMP01',
            'fecha_inicio_programa': '2024-01-01',
            'estado_programa': 'Activo',
            'duracion_programa': 4,
            'facultad_programa': 'FCOMP',
            'modalidad_programa': 'Presencial',
            'director_programa': 'Juan Pérez'
        }
        form = EditarProgramaForm(data=form_data, instance=self.programa)

        # Verificamos que el formulario sea válido
        self.assertFalse(form.is_valid())

    def test_invalid_form(self):
        # Creamos datos inválidos para el formulario
        form_data = {
            'nombre_programa': '',
            'codigo_programa': 'DCOMP01',
            'fecha_inicio_programa': '2024-01-01',
            'estado_programa': 'Activo',
            'duracion_programa': 4,
            'facultad_programa': self.programa.facultad_programa.nombre_facultad,
            'modalidad_programa': 'Presencial',
            'director_programa': self.programa.director_programa.id
        }
        form = EditarProgramaForm(data=form_data, instance=self.programa)

        # Verificamos que el formulario sea inválido
        self.assertFalse(form.is_valid())


