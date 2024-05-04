import pytest
from CCSApp.models import Director_de_programa

@pytest.mark.django_db
def test_director_programa_creation():
    director = Director_de_programa.objects.create(
        nombre_director='Juan Pérez',
        numero_director='123456789',
        correo_director='juanperez@example.com'
    )
    assert director.nombre_director == 'Juan Pérez'
