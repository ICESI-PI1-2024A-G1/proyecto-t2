import pytest
from CCSApp.models import Actividad, Evento, Espacio

@pytest.mark.django_db
def test_actividad_creation():
    # Creamos un evento asociado a la actividad
    
    espacio = Espacio.objects.create(
        espacio_codigo='A101',
        capacidad_espacio=50,
        tipo='Salon'
    )
    
    evento = Evento.objects.create(
        nombre_evento='Seminario de Inteligencia Artificial',
        fecha_inicio_evento='2024-05-10',
        fecha_finalizacion_evento='2024-05-12',
        lugar_evento=espacio,
        descripcion_evento='Un seminario sobre los últimos avances en inteligencia artificial.'
    )

    # Creamos una actividad relacionada con el evento
    actividad = Actividad.objects.create(
        nombre_actividad='Conferencia inaugural',
        descripcion_actividad='Presentación de los temas a tratar en el seminario.',
        duracion_en_horas=1,
        orador_actividad='Dr. Juan Pérez',
        evento_actividad=evento
    )

    # Verificamos que la actividad se haya creado correctamente
    assert actividad.nombre_actividad == 'Conferencia inaugural'

@pytest.mark.django_db
def test_actividad_creation_nombre_incorrecto():
        # Creamos un evento asociado a la actividad
        espacio = Espacio.objects.create(
            espacio_codigo='A101',
            capacidad_espacio=50,
            tipo='Salon'
        )

        evento = Evento.objects.create(
            nombre_evento='Seminario de Inteligencia Artificial',
            fecha_inicio_evento='2024-05-10',
            fecha_finalizacion_evento='2024-05-12',
            lugar_evento=espacio,
            descripcion_evento='Un seminario sobre los últimos avances en inteligencia artificial.'
        )

        # Creamos una actividad con nombre incorrecto
        actividad = Actividad.objects.create(
            nombre_actividad='Conferencia incorrecta',  # Nombre incorrecto
            descripcion_actividad='Presentación de los temas a tratar en el seminario.',
            duracion_en_horas=1,
            orador_actividad='Dr. Juan Pérez',
            evento_actividad=evento
        )

        # Verificamos que la actividad tenga el nombre incorrecto
        assert actividad.nombre_actividad != 'Conferencia inaugural'  # Resultado esperado: False
    
