import pytest
from CCSApp.models import *

@pytest.mark.django_db
def test_nrc_creation():
    periodo = Periodo.objects.create(id_periodo='2024A', fecha_inicio_periodo = '2005-02-02', fecha_final_periodo='2005-05-02')
    departamento = Departamento.objects.create(id_departamento='001', nombre_departamento='Departamento de Ingeniería de Software')
    semestre = Semestre.objects.create(nombre_semestre='2024-1', estado_semestre='Activo', año=2024, periodo=1)
    materia = Materia.objects.create(nombre_materia='Introducción a la Ingeniería de Software', codigo_materia='IS101', creditos_materia=3, departamento=departamento, semestre=semestre)

    nrc = Nrc.objects.create(id_nrc='001', periodo_nrc=periodo, grupo=1, materia_nrc=materia)
    assert nrc.id_nrc == '001'

