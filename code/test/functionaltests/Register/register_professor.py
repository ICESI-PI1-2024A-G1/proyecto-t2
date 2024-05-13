import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterProfesorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_register_profesor(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        self.assertIn('Iniciar Sesión', driver.title)
        
        # Introduce las credenciales y haz clic en Iniciar Sesión
        username_input = driver.find_element(By.NAME, 'cedula')
        password_input = driver.find_element(By.NAME, 'password')
        username_input.send_keys('1023456325')
        password_input.send_keys('dorits123')
        login_button = driver.find_element(By.NAME, 'btn_iniciar')
        login_button.click()
        
        # Espera hasta que la página se cargue después del inicio de sesión
        WebDriverWait(driver, 10).until(
            EC.title_contains('CCSA')
        )

        # Verifica que el título de la página sea 'CCSA'
        self.assertIn('CCSA', driver.title)
        
        # Ahora, realiza el registro de un profesor
        driver.find_element(By.XPATH, '//button[text()="Servicios de Asignacion"]').click()
        driver.find_element(By.XPATH, '//button[text()="Registrar Profesor"]').click()
        driver.find_element(By.ID, 'nombre_completo').send_keys('Norha Villegas')
        driver.find_element(By.ID, 'identificacion_profesor').send_keys('68298420')
        driver.find_element(By.ID, 'especializacion').send_keys('Doctorado en Gestión informática organizativa')
        driver.find_element(By.ID, 'correo_electronico_profe').send_keys('nvillega@u.icesi.edu.co')
        driver.find_element(By.ID, 'telefono').send_keys('3195627853')
        driver.find_element(By.ID, 'Guardar').click()

        # Puedes agregar más lógica de espera o verificaciones aquí si es necesario
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
