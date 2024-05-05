import pytest
from CCSApp.models import Evento, Espacio

@pytest.mark.django_db
def test_evento_creation():
    # Creamos un espacio donde se llevará a cabo el evento
    espacio = Espacio.objects.create(
        espacio_codigo='A101',
        capacidad_espacio=50,
        tipo='Salon'
    )

    # Creamos un evento
    evento = Evento.objects.create(
        nombre_evento='Conferencia de Ciencias de la Computación',
        fecha_inicio_evento='2024-06-15',
        fecha_finalizacion_evento='2024-06-17',
        lugar_evento=espacio,
        descripcion_evento='Una conferencia sobre los avances más recientes en ciencias de la computación.'
    )

    # Verificamos que el evento se haya creado correctamente
    assert evento.nombre_evento == 'Conferencia de Ciencias de la Computación'
