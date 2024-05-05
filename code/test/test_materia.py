import pytest
from CCSApp.models import Materia, Departamento, Semestre
from django.test import RequestFactory
from CCSApp.views import buscar_materia
from CCSApp.forms import MateriaSearchForm
@pytest.mark.django_db
def test_materia_creation():
    departamento = Departamento.objects.create(id_departamento='001', nombre_departamento='Departamento de Ingeniería de Software')
    semestre = Semestre.objects.create(nombre_semestre='2024-1', estado_semestre='Activo', año=2024, periodo=1)
    materia = Materia.objects.create(nombre_materia='Introducción a la Ingeniería de Software', codigo_materia='IS101', creditos_materia=3, departamento=departamento, semestre=semestre)
    assert materia.nombre_materia == 'Introducción a la Ingeniería de Software'


@pytest.mark.django_db
def test_buscar_materia_view():
    # Creamos una materia para probar
    materia = Materia.objects.create(nombre_materia='Matemáticas', codigo_materia='MAT101', creditos_materia=3)

    # Creamos un request ficticio con método POST y datos de formulario
    request = RequestFactory().post('/buscar-materia/', {'nombre_materia': 'Mat'})

    # Ejecutamos la vista
    response = buscar_materia(request)

    # Verificamos que se haya renderizado correctamente la plantilla
    assert response.status_code == 200

    # Verificamos que el formulario esté presente en el contexto de la respuesta
    assert 'form' in response.context

    # Verificamos que la materia se haya filtrado correctamente
    materias = response.context['materias']
    assert materias.count() == 1
