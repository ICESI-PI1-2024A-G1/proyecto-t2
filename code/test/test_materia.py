import pytest
from CCSApp.models import Materia, Departamento, Semestre

@pytest.mark.django_db
def test_materia_creation():
    departamento = Departamento.objects.create(id_departamento='001', nombre_departamento='Departamento de Ingeniería de Software')
    semestre = Semestre.objects.create(nombre_semestre='2024-1', estado_semestre='Activo', año=2024, periodo=1)
    materia = Materia.objects.create(nombre_materia='Introducción a la Ingeniería de Software', codigo_materia='IS101', creditos_materia=3, departamento=departamento, semestre=semestre)
    assert materia.nombre_materia == 'Introducción a la Ingeniería de Software'
