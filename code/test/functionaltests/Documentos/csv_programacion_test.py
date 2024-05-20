import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DescargarCsvProgramacionTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
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

        csvprogramacion_btn = driver.find_element(By.NAME,'csv_programacion_btn')
        csvprogramacion_btn.click()

        time.sleep(15)

        

        # Verificar que el archivo se haya descargado correctamente
        downloaded_file_path = "C:/Users/Isabella/Descargas/ReporteProgramacionAcademica.xlsx"
    
    
        # Realizar el assert sobre el archivo descargado, por ejemplo, verificar el nombre del archivo
        expected_file_name = "ReporteProgramacionAcademica.xlsx"
        actual_file_name = os.path.basename(downloaded_file_path)
        self.assertEqual(actual_file_name, expected_file_name, "El nombre del archivo descargado no es el esperado")

        


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()