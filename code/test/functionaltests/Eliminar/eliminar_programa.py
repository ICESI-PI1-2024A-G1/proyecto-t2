import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class EliminarProgramaTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

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
        
        # Espera hasta que la página se cargue después del inicio de sesión
        WebDriverWait(driver, 10).until(
            EC.title_contains('CCSA')
        )

        # Verifica que el título de la página sea 'CCSA'
        self.assertIn('CCSA', driver.title)

        gestion_button = driver.find_element(By.NAME, 'btn_gestion')
        gestion_button.click()

        WebDriverWait(driver, 4).until(
            EC.title_contains('Gestion de Información')
        )


        eliminar_programa_btn = driver.find_element(By.NAME, 'eliminarp_btn')
        eliminar_programa_btn.click()

        WebDriverWait(driver, 4).until(
            EC.title_contains('Consultar Programas Academicos')
        )
        
        image_button = driver.find_element(By.XPATH, '//*[@id="page1"]/div[2]/div/table/tbody/tr[1]/td[8]/a/div/img')
        image_button.click()

        # Espera hasta que se cargue la página después del registro
        WebDriverWait(driver, 10).until(
            EC.title_contains('Consultar Programas Academicos')
        )

        # Verifica que el título de la página sea 'Inicio'
        self.assertIn('Consultar Programas Academicos', driver.title)
        


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
