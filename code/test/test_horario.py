import pytest
from CCSApp.models import Horario, Materia, Espacio
from datetime import date, time

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
