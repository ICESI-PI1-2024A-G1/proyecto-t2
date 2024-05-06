import pytest

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
    
    
