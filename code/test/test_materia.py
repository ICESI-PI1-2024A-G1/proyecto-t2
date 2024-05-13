import pytest
from CCSApp.models import Materia, Departamento, Semestre
from django.test import TestCase
from CCSApp.forms import MateriaSearchForm
@pytest.mark.django_db
def test_materia_creation():
    departamento = Departamento.objects.create(id_departamento='001', nombre_departamento='Departamento de Ingeniería de Software')
    semestre = Semestre.objects.create(nombre_semestre='2024-1', estado_semestre='Activo', año=2024, periodo=1)
    materia = Materia.objects.create(nombre_materia='Introducción a la Ingeniería de Software', codigo_materia='IS101', creditos_materia=3, departamento=departamento, semestre=semestre)
    assert materia.nombre_materia == 'Introducción a la Ingeniería de Software'


class TestMateriaSearchForm(TestCase):
    def test_valid_form(self):
        # Creamos datos válidos para el formulario
        form_data = {'nombre_materia': 'Introducción a la Ingeniería de Software'}
        form = MateriaSearchForm(data=form_data)

        # Verificamos que el formulario sea válido
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Creamos datos inválidos para el formulario
        form_data = {'nombre_materia': ''}
        form = MateriaSearchForm(data=form_data)

        # Verificamos que el formulario sea inválido
        self.assertFalse(form.is_valid())
        
