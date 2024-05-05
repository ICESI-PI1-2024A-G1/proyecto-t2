import pytest
from django.test import RequestFactory
from django.contrib.auth.models import User
from CCSApp.models import Usuario
from CCSApp.views import log_in

from CCSApp.models import *

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
def test_log_in_view():
    # Creamos un usuario para utilizarlo en las pruebas
    user = Usuario.objects.create(
        nombre='Usuario Prueba',
        cedula='1234567890',
        rol='admin',
        departamento='TIC',
        correo_electronico='usuario@example.com',
        telefono=123456789,
        password='password123'
    )

    # Creamos una solicitud HTTP POST con datos de formulario válidos
    request = RequestFactory().post('', {
        'cedula': '1234567890',
        'password': 'password123'
    })

    # Agregamos el usuario autenticado en la solicitud
    request.user = user

    # Llamamos a la vista y obtenemos la respuesta
    response = log_in(request)

    # Verificamos que la respuesta sea una redirección
    assert response.status_code == 302

    # Verificamos que la redirección se haga a la página de inicio correcta
    assert response.url == '/index/'

    # También podemos probar un escenario donde las credenciales no son válidas
    # Creamos una solicitud HTTP POST con datos de formulario inválidos
    request_invalid = RequestFactory().post('', {
        'cedula': '1234567890',
        'password': 'claveincorrecta'
    })

    # Llamamos a la vista con las credenciales inválidas
    response_invalid = log_in(request_invalid)

    # Verificamos que la vista renderice la plantilla de inicio de sesión nuevamente
    assert response_invalid.status_code == 200

    # Verificamos que el mensaje de error sea visible en la respuesta renderizada
    assert 'Usuario o clave incorrecta, intente de nuevo' in response_invalid.content.decode('utf-8')