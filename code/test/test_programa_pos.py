import pytest
from CCSApp.models import Programa_de_posgrado, Facultad, Director_de_programa
from datetime import date

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