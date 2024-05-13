from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.conf import settings

settings.configure(
            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'DJANGO_SETTINGS_MODULE',
                'CCSApp'
            ]
        )

class LoginFunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        cls.selenium.implicity_wait(4)
    
    def login_test(self):
        
        self.selenium.get(self.live_server_url)

        username_input = self.selenium.find_element(By.ID, 'id_cedula')
        password_input = self.selenium.find_element(By.ID, 'id_password')
        username_input.send_keys('2345549302')
        password_input.send_keys('Doris123')

        password_input.send_keys(Keys.RETURN)

        self.assertIn('CCSA', self.selenium.title)