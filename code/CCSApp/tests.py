from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from .forms import *

class NewHorarioFormTests(TestCase):

    def test_invalid_modalidad(self):
        # Prueba con modalidad inválida
        form_data = {
            'fecha_hora': '2024-03-17T12:00',
            'profesor': 'Juan Perez',
            'materia': '445688',
            'modalidad': 'invalida',  # Modalidad no válida
            'salon_presencial': '201C',
        }
        form = NewHorario(data=form_data)
        self.assertFalse(form.is_valid())  # Debe ser inválido debido a la modalidad

    def test_empty_data(self):
        # Prueba con datos vacíos
        form = NewHorario(data={})
        self.assertFalse(form.is_valid())  # Debe ser inválido debido a campos requeridos
    class EspacioTestCase(TestCase):
        def test_creacion_espacio(self):
            # Crea un objeto de prueba para el formulario
            form_data = {
                'nombre': 'Salón 1',
                'ubicacion': 'Edificio A',
                'capacidad': 50,
                'disponibilidad': 'Disponible',
                'tipo': 'salon',
            }
            form = EspacioForm(data=form_data)

            # Verifica que el formulario es válido
            self.assertTrue(form.is_valid())

            # Guarda el objeto de espacio en la base de datos
            espacio = form.save()

            # Verifica que el objeto de espacio se haya guardado correctamente
            self.assertEqual(Espacio.objects.count(), 1)

            # Verifica que los atributos del objeto de espacio son correctos
            self.assertEqual(espacio.nombre, 'Salón 1')
            self.assertEqual(espacio.ubicacion, 'Edificio A')
            self.assertEqual(espacio.capacidad, 50)
            self.assertEqual(espacio.disponibilidad, 'Disponible')
            self.assertEqual(espacio.tipo, 'salon')
        def test_vista_creacion_espacio(self):
        # Obtiene la URL para la vista de creación de espacios
            url = reverse('crear_espacio')  # Reemplaza 'crear_espacio' con el nombre de la vista

            # Realiza una solicitud POST al formulario de creación de espacios
            response = self.client.post(url, {
                'nombre': 'Salón 2',
                'ubicacion': 'Edificio B',
                'capacidad': 30,
                'disponibilidad': 'Disponible',
                'tipo': 'salon',
            })

            # Verifica que la respuesta redirija a la página de lista de espacios
            self.assertRedirects(response, reverse('ruta_hacia_lista_de_espacios'))
            
    class EditarProgramaAcademicoTestCase(TestCase):
        def setUp(self):
            self.client = Client()
            self.programa = Programa_de_posgrado.objects.create(name='Programa de Prueba', codigo='PRB123', descripcion='Descripción de prueba', fecha_inicio='2024-01-01', fecha_finalizacion='2024-12-31', value=1000, duracion='6 meses', modalidad='Presencial')
            self.url = reverse('editar_programa', args=[self.programa.codigo])

        def test_editar_programa_academico_get(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'editar_programa.html')

        def test_editar_programa_academico_post(self):
            data = {
                'name': 'Programa Modificado',
                'codigo': 'MOD123',
                'descripcion': 'Nueva descripción',
                'fecha_inicio': '2025-01-01',
                'fecha_finalizacion': '2025-12-31',
                'value': 1500,
                'duracion': '12 meses',
                'modalidad': 'Virtual'
            }
            response = self.client.post(self.url, data)
            self.assertEqual(response.status_code, 302)  # Debería redirigir después de la edición
            programa_modificado = Programa_de_posgrado.objects.get(pk=self.programa.pk)
            self.assertEqual(programa_modificado.name, 'Programa Modificado')
            # Verificar otros campos modificados según sea necesario