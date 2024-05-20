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

@pytest.mark.django_db
def test_director_programa_creation_valid_name():
    director = Director_de_programa.objects.create(
        nombre_director='María Gómez',
        numero_director='987654321',
        correo_director='mariagomez@example.com'
    )
    assert director.nombre_director == 'María Gómez'

@pytest.mark.django_db
def test_director_programa_creation_valid_phone_number():
    director = Director_de_programa.objects.create(
        nombre_director='Pedro López',
        numero_director='+57 312 3456789',
        correo_director='pedrolopez@example.com'
    )
    assert director.numero_director == '+57 312 3456789'
