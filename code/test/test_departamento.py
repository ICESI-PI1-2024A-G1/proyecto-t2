import pytest
from CCSApp.models import Departamento

@pytest.mark.django_db
def test_departamento_creation():
    departamento = Departamento.objects.create(id_departamento='001', nombre_departamento='Departamento de Ingeniería de Software')
    assert departamento.id_departamento == '001'

@pytest.mark.django_db
def test_departamento_creation_valid_id():
    departamento = Departamento.objects.create(id_departamento='002', nombre_departamento='Departamento de Sistemas de Información')
    assert departamento.id_departamento == '002'

@pytest.mark.django_db
def test_departamento_creation_valid_name():
    departamento = Departamento.objects.create(id_departamento='003', nombre_departamento='Departamento de Ciencia de Datos')
    assert departamento.nombre_departamento == 'Departamento de Ciencia de Datos'


