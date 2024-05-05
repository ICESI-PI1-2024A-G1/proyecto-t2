import pytest

from CCSApp.models import Profesor

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