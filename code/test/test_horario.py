import pytest
from CCSApp.models import Horario, Materia, Espacio
from datetime import date, datetime, time

@pytest.mark.django_db
def test_horario_creation():
    materia = Materia.objects.create(nombre_materia='Matemáticas', codigo_materia='MAT101', creditos_materia=3)
    espacio = Espacio.objects.create(espacio_codigo='A101', capacidad_espacio=50, tipo='Salon')

    horario = Horario.objects.create(
        fecha_inicio_horario=date.today(),
        hora_inicio_horario=time(8, 0),
        hora_final_horario=time(10, 0),
        materia=materia,
        grupo='001',
        modalidad='presencial',
        salon_presencial=espacio
    )
    assert horario.grupo == '001'

@pytest.mark.django_db
def test_horario_creation_valid_data():
    materia = Materia.objects.create(nombre_materia='Física', codigo_materia='FIS102', creditos_materia=4)
    espacio = Espacio.objects.create(espacio_codigo='A202', capacidad_espacio=30, tipo='Laboratorio')

    horario = Horario.objects.create(
        fecha_inicio_horario=date.today(),
        hora_inicio_horario=time(11, 0),
        hora_final_horario=time(13, 0),
        materia=materia,
        grupo='002',
        modalidad='presencial',
        salon_presencial=espacio
    )

    assert horario.fecha_inicio_horario == date.today()
    assert horario.hora_inicio_horario == time(11, 0)
    assert horario.hora_final_horario == time(13, 0)
    assert horario.materia == materia
    assert horario.grupo == '002'
    assert horario.modalidad == 'presencial'
    assert horario.salon_presencial == espacio

