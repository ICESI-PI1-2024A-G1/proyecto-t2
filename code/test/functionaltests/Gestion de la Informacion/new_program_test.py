import random
import string
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class CrearProgramaTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_random_codigo(self):
        return ''.join(random.choices(string.digits, k=6))  # Suponiendo que el código tiene 6 dígitos

    def generate_random_fecha(self):
        # Genera una fecha aleatoria en formato dd/mm/aaaa
        return f"{random.randint(1, 28)}/{random.randint(1, 12)}/{random.randint(2000, 2024)}"

    def generate_random_duracion(self):
        return random.randint(1, 6)  # Suponiendo que la duración es un número entre 1 y 6 años

    def test_crear_programa(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000')
        self.assertIn('Iniciar Sesión', driver.title)
        username_input = driver.find_element(By.NAME, 'cedula')
        password_input = driver.find_element(By.NAME, 'password')
        username_input.send_keys('1023456325')
        password_input.send_keys('dorits123')

        # Encuentra el botón de "Iniciar sesión" y haz clic en él
        login_button = driver.find_element(By.NAME, 'btn_iniciar')
        login_button.click()

        WebDriverWait(driver, 4).until(
            EC.title_contains('CCSA')
        )

        gestion_button = driver.find_element(By.NAME, 'btn_gestion')
        gestion_button.click()

        WebDriverWait(driver, 4).until(
            EC.title_contains('Gestion de Información')
        )


        nprograma_button = driver.find_element(By.NAME, 'crearp_btn')
        nprograma_button.click()

        WebDriverWait(driver, 4).until(
            EC.title_contains('Crear Programa Académico')
        )
        

        facultades_posibles = ['1 - Facultad de Negocios y Economía', '	2 - Facultad de Ingeniería, Diseño y Ciencias Aplicadas', '	3 - Facultad de Ciencias Humanas', '4 - Facultad de Ciencias de la Salud']
        estados_posibles = ['Activo', 'Inactivo']
        modalidades_posibles = ['Presencial', 'Virtual', 'Mixto']
        directores_posibles = ['Andrés Felipe Millán Cifuentes', 'Juan David Horca']

        # Genera datos de entrada aleatorios
        nombre_programa = self.generate_random_string()
        codigo_programa = self.generate_random_codigo()
        fecha_inicio = self.generate_random_fecha()
        estado_programa = random.choice(estados_posibles)
        duracion_programa = self.generate_random_duracion()
        facultad_programa = random.choice(facultades_posibles)
        modalidad_programa = random.choice(modalidades_posibles)
        director_programa = random.choice(directores_posibles)
        
        # Encuentra los campos de registro
        nombreprograma_input = driver.find_element(By.NAME, 'nombre_programa')
        codigo_input = driver.find_element(By.NAME, 'codigo_programa')
        fecha_inicio_input = driver.find_element(By.NAME, 'fecha_inicio_programa')
        estado_input  = driver.find_element(By.NAME, 'estado_programa')
        duracion_input  = driver.find_element(By.NAME, 'duracion_programa')
        facultad_input  = driver.find_element(By.NAME, 'facultad_programa')
        modalidad_input  = driver.find_element(By.NAME, 'modalidad_programa')
        director_input  = driver.find_element(By.NAME, 'director_programa')

        # Llena los campos de registro
        nombreprograma_input.send_keys(nombre_programa)
        codigo_input.send_keys(codigo_programa)
        fecha_inicio_input.send_keys(fecha_inicio)
        estado_select = Select(estado_input)
        estado_select.select_by_index(random.randint(0, len(estados_posibles) - 1))
        duracion_input.send_keys(str(duracion_programa))  # Convertir a string
        facultad_select = Select(facultad_input)
        facultad_select.select_by_index(random.randint(0, len(facultades_posibles) - 1))
        modalidad_select = Select(modalidad_input)
        modalidad_select.select_by_index(random.randint(0, len(modalidades_posibles) - 1))
        director_select = Select(director_input)
        director_select.select_by_index(random.randint(0, len(modalidades_posibles) - 1))
        

        # Encuentra el botón de registro y haz clic en él
        guardar_button = driver.find_element(By.NAME, 'Guardar_btn')
        guardar_button.click()
        
        # Espera hasta que se cargue la página después del registro
        WebDriverWait(driver, 10).until(
            EC.title_contains('Gestion de Información')
        )

        # Verifica que el título de la página sea 'Inicio'
        self.assertIn('Gestion de Información', driver.title)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
