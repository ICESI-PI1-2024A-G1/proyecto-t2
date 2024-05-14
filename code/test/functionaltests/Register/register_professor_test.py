import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestRegisterProfesor(unittest.TestCase):
    # Inicializar el driver de Chrome con las opciones
    
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--force-device-scale-factor=0.8")
        self.driver = webdriver.Chrome(options=chrome_options)

    

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
        
        WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, '.bloq-sup_secd'))
)

        # Hacer clic en el elemento utilizando JavaScript
        element = driver.find_element(By.XPATH, '//button[text()="Servicios de Asignacion"]')
        driver.execute_script("arguments[0].click();", element)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Registrar Profesor"]'))
        ).click()
        
        # Espera hasta que el campo de entrada 'nombre_profesor' esté presente y sea interactuable
        nombre_profesor_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'nombre_profesor'))
        )
        nombre_profesor_input.send_keys('Norha Villegas')

        identificacion_profesor_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'cedula_profesor'))
        )
        identificacion_profesor_input.send_keys('68298420')

        especializacion_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'especializacion_profesor'))
        )
        especializacion_input.send_keys('Doctorado en Gestión informática organizativa')

        correo_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'correo_electronico'))
        )
        correo_input.send_keys('nvillega@u.icesi.edu.co')

        telefono_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'telefono'))
        )
        telefono_input.send_keys('3195627853')
        
        # Haz clic en el botón "Guardar"
        guardar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Guardar"]'))
        )
        guardar_button.click()

        # Puedes agregar más lógica de espera o verificaciones aquí si es necesario
        

    def test_register_existing_profesor(self):
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
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Registrar Profesor"]'))
        ).click()
        
        # Espera hasta que el campo de entrada 'nombre_profesor' esté presente y sea interactuable
        nombre_profesor_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'nombre_profesor'))
        )
        nombre_profesor_input.send_keys('Nicolas Salazar')

        identificacion_profesor_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'cedula_profesor'))
        )
        identificacion_profesor_input.send_keys('68298420')

        especializacion_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'especializacion_profesor'))
        )
        especializacion_input.send_keys('Doctorado en Gestión informática organizativa')

        correo_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'correo_electronico'))
        )
        correo_input.send_keys('nvillega@u.icesi.edu.co')

        telefono_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'telefono'))
        )
        telefono_input.send_keys('3195627853')
        
        # Haz clic en el botón "Guardar"
        guardar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Guardar"]'))
        )
        guardar_button.click()

        # Verifica que se muestre un mensaje de error indicando que el profesor ya existe
        mensaje_error = driver.execute_script('return document.getElementById("modal-error").textContent')

        # Imprimir el mensaje de error obtenido
        print("Mensaje de error:", mensaje_error)
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
