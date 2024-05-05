import pytest
from CCSApp.models import *

@pytest.mark.django_db
def test_semestre_creation():
    # Creamos un programa de posgrado
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

    # Creamos un semestre y lo relacionamos con el programa de posgrado
    semestre = Semestre.objects.create(nombre_semestre='2024-1', estado_semestre='Activo', año=2024, periodo=1)
    semestre.programa_semestre.add(programa)

    # Verificamos que el semestre se haya creado correctamente
    assert semestre.nombre_semestre == '2024-1'
