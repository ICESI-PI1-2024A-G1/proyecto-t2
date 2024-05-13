import pytest
from CCSApp.models import Espacio, Edificio
from django.test import TestCase
from CCSApp.forms import EditarEspacio



@pytest.mark.django_db
def test_espacio_creation():
    # Creamos un edificio asociado al espacio
    edificio = Edificio.objects.create(
        nombre_edificio='Edificio A',
        numero_espacios=10
    )

    # Creamos un espacio
    espacio = Espacio.objects.create(
        espacio_codigo='A101',
        capacidad_espacio=50,
        edificio_espacio=edificio,
        disponibilidad_espacio='Disponible',
        tipo='Salon'
    )

    # Verificamos que el espacio se haya creado correctamente
    assert espacio.espacio_codigo == 'A101'


class TestEditarEspacioForm(TestCase):
    def setUp(self):
        # Creamos una instancia de Edificio para usar en las pruebas
        self.edificio = Edificio.objects.create(nombre_edificio='Edificio A', numero_espacios=10)

        # Creamos un espacio para usar en las pruebas
        self.espacio = Espacio.objects.create(
            espacio_codigo='A101',
            capacidad_espacio=50,
            edificio_espacio=self.edificio,
            disponibilidad_espacio='Disponible',
            tipo='Salon'
        )

    def test_valid_form(self):
        # Creamos datos válidos para el formulario
        form_data = {
            'espacio_codigo': 'A101',
            'capacidad_espacio': 50,
            'edificio_espacio': self.edificio.nombre_edificio,
            'disponibilidad_espacio': 'Disponible',
            'tipo': 'Salon'
        }
        form = EditarEspacio(data=form_data, instance=self.espacio)

        # Verificamos que el formulario sea válido
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Creamos datos inválidos para el formulario
        form_data = {
            'espacio_codigo': '',
            'capacidad_espacio': 50,
            'edificio_espacio': self.edificio.nombre_edificio,
            'disponibilidad_espacio': 'Disponible',
            'tipo': 'Salon'
        }
        form = EditarEspacio(data=form_data, instance=self.espacio)

        # Verificamos que el formulario sea inválido
        self.assertFalse(form.is_valid())

