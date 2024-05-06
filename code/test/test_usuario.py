import pytest

from CCSApp.models import Usuario
from django.test import TestCase, Client
from CCSApp.forms import LoginForm
from django.urls import reverse



@pytest.mark.django_db
def test_usuario_creation():
    usuario = Usuario.objects.create(
        nombre = 'Fernando Hernandez',
        cedula = '123456789',
        rol = 'admin',
        departamento = 'TIC',
        correo_electronico = 'fernandoh@gmail.com',
        telefono = 32141643,
        password = 'jiji'
        
    )
    assert usuario.cedula == '123456789'
    
@pytest.mark.django_db
class TestLoginForm(TestCase):
    def test_valid_form(self):
        # Creamos datos válidos para el formulario
        form_data = {'cedula': '1234567890', 'password': 'password123'}
        form = LoginForm(data=form_data)

        # Verificamos que el formulario sea válido
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Creamos datos inválidos para el formulario
        form_data = {'cedula': '', 'password': ''}
        form = LoginForm(data=form_data)

        # Verificamos que el formulario sea inválido
        self.assertFalse(form.is_valid())
        


