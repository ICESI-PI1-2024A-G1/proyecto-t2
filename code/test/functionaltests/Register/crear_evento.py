import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class CrearEventoTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--force-device-scale-factor=0.8")
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_register_evento(self):
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
        
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.bloq-sup_secd'))
        )

        # Hacer clic en el elemento "Servicios de Asignacion"
        element = driver.find_element(By.XPATH, '//button[text()="Servicios de Asignacion"]')
        driver.execute_script("arguments[0].click();", element)

        # Hacer clic en el botón "Registrar Evento"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Crear Evento"]'))
        ).click()
        
        # Esperar hasta que los campos estén presentes y sean interactuables
        nombre_evento_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'nombre_evento'))
        )
        nombre_evento_input.send_keys('Conferencia de Diseño')

        fecha_inicio_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'fecha_inicio_evento'))
        )
        fecha_inicio_input.send_keys('2024-05-20')

        fecha_final_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'fecha_finalizacion_evento'))
        )
        fecha_final_input.send_keys('2024-05-22')

        lugar_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'lugar_evento'))
        )
        lugar_select.send_keys('303-Edificio D')

        descripcion_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'descripcion_evento'))
        )
        descripcion_input.send_keys('Conferencia sobre diseño gráfico y UX')

        programa_posgrado_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'programa_de_posgrado_evento'))
        )
        programa_posgrado_select.send_keys('Maestría en Diseño de Experiencia de Usuario')

        # Hacer clic en el botón "Guardar"
        guardar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Guardar"]'))
        )
        guardar_button.click()

        # Puedes agregar más lógica de espera o verificaciones aquí si es necesario
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
