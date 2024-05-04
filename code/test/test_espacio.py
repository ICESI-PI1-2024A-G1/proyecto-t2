import pytest
from CCSApp.models import Espacio, Edificio

@pytest.mark.django_db
def test_espacio_creation():
    # Creamos un edificio asociado al espacio
    edificio = Edificio.objects.create(
        nombre_edificio='Edificio A',
        numero_espacios=10
    )

    # Creamos un espacio
    espacio = Espacio.objects.create(
        espacio_codigo='A101',
        capacidad_espacio=50,
        edificio_espacio=edificio,
        disponibilidad_espacio='Disponible',
        tipo='Salon'
    )

    # Verificamos que el espacio se haya creado correctamente
    assert espacio.espacio_codigo == 'A101'
