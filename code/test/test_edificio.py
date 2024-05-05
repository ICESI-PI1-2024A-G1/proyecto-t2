import pytest
from CCSApp.models import Edificio

@pytest.mark.django_db
def test_edificio_creation():
    # Creamos un edificio
    edificio = Edificio.objects.create(
        nombre_edificio='Edificio A',
        numero_espacios=10
    )

    # Verificamos que el edificio se haya creado correctamente
    assert edificio.nombre_edificio == 'Edificio A'
