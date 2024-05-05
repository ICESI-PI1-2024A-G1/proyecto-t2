import pytest
from CCSApp.models import Departamento

@pytest.mark.django_db
def test_departamento_creation():
    departamento = Departamento.objects.create(id_departamento='001', nombre_departamento='Departamento de Ingeniería de Software')
    assert departamento.id_departamento == '001'

