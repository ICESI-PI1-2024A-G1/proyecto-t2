import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestRegisterMateria(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--force-device-scale-factor=0.8")
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_register_materia(self):
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

        # Hacer clic en el elemento utilizando JavaScript
        element = driver.find_element(By.XPATH, '//button[text()="Servicios de Asignacion"]')
        driver.execute_script("arguments[0].click();", element)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Registrar Materia"]'))
        ).click()
        
        # Espera hasta que el campo de entrada 'nombre_materia' esté presente y sea interactuable
        nombre_materia_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'nombre_materia'))
        )
        nombre_materia_input.send_keys('Fundamentos UX')

        codigo_materia_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'codigo_materia'))
        )
        codigo_materia_input.send_keys('123456')

        creditos_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'creditos_materia'))
        )
        creditos_input.send_keys('4')

        # Subir archivo
        archivo_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'syllabus'))
        )
        archivo_input.send_keys("C:\\Users\\user\\OneDrive\\Documentos\\Formato.pdf")  # Ruta del archivo en tu sistema

        departamento_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'departamento'))
        )
        departamento_select.send_keys('DIS-Diseño')

        semestre_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'semestre'))
        )
        semestre_select.send_keys('2023-2')

        # Haz clic en el botón "Guardar"
        guardar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Guardar"]'))
        )
        guardar_button.click()

        # Puedes agregar más lógica de espera o verificaciones aquí si es necesario
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
