import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class EditarMateriaTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--force-device-scale-factor=0.8")
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_editar_materia(self):
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

        # Hacer clic en el botón "Editar Materia"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Editar Materia"]'))
        ).click()
        
        # Esperar hasta que el campo de entrada 'nombre_materia' esté presente y sea interactuable
        nombre_materia_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'nombre_materia'))
        )
        nombre_materia_input.send_keys('Analitica para los negocios')

        # Hacer clic en el botón "Buscar"
        buscar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Buscar"]'))
        )
        buscar_button.click()

        # Seleccionar la materia encontrada
        materia_encontrada = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="div_Table2"]//table//tbody//tr//td//a[contains(text(), "Fundamentos UX")]'))
        )
        materia_encontrada.click()

        # Cambiar el campo de departamento
        departamento_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'departamento'))
        )
        departamento_select.send_keys('ECO-Economia')

        # Hacer clic en el botón "Guardar Cambios"
        guardar_cambios_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Guardar Cambios"]'))
        )
        guardar_cambios_button.click()

        # Puedes agregar más lógica de espera o verificaciones aquí si es necesario
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
