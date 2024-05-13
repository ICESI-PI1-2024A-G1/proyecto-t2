import random
import string
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def generate_random_name(self, length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_random_cedula(self):
        return ''.join(random.choices(string.digits, k=10))  # Una cédula típica tiene 10 dígitos

    def generate_random_rol(self):
        roles = ['Gestor', 'Lider', 'Director']  # Lista de roles posibles
        return random.choice(roles)

    def generate_random_department(self):
        departments = ['Departamento 1', 'Departamento 2', 'Departamento 3']  # Lista de departamentos posibles
        return random.choice(departments)

    def generate_random_email(self, length=8):
        return self.generate_random_name(length) + '@example.com'

    def generate_random_phone(self):
        return ''.join(random.choices(string.digits, k=10))  # Un número de teléfono típico tiene 10 dígitos

    def generate_random_password(self, length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def test_register(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000')
        self.assertIn('Iniciar Sesión', driver.title)


        register_button1 = driver.find_element(By.NAME, 'btn_registrar')
        register_button1.click()

        time.sleep(4)

        self.assertIn('Registro', driver.title)

        # Genera datos de entrada aleatorios
        name = self.generate_random_name()
        cedula = self.generate_random_cedula()
        rol = self.generate_random_rol()
        department = self.generate_random_department()
        email = self.generate_random_email()
        phone = self.generate_random_phone()
        password = self.generate_random_password()
        
        # Encuentra los campos de registro
        nombre_input = driver.find_element(By.NAME, 'nombre')
        cedula_input = driver.find_element(By.NAME, 'cedula')
        rol_input = driver.find_element(By.NAME, 'rol')
        departamento_input = driver.find_element(By.NAME, 'departamento')
        correo_input  = driver.find_element(By.NAME, 'correo_electronico')
        telefono_input  = driver.find_element(By.NAME, 'telefono')
        password_input  = driver.find_element(By.NAME, 'password')
        
        # Llena los campos de registro
        nombre_input.send_keys(name)
        cedula_input.send_keys(cedula)
        rol_input.send_keys(rol)
        departamento_input.send_keys(department)
        correo_input.send_keys(email)
        telefono_input.send_keys(phone)
        password_input.send_keys(password)

        # Encuentra el botón de registro y haz clic en él
        register_button = driver.find_element(By.NAME, 'registrar')
        register_button.click()
        
        # Espera hasta que se cargue la página después del registro
        WebDriverWait(driver, 10).until(
            EC.title_contains('Iniciar Sesión')
        )

        # Verifica que el título de la página sea 'Inicio'
        self.assertIn('Iniciar Sesión', driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
