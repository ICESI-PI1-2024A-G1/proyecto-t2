from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path= "chromedriver.exe")
driver = webdriver.Chrome(service = service)

driver.get("http://127.0.0.1:8000/")

time.sleep(2)
driver.quit()