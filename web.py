from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\Eliot Aldersson\\Downloads\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(2)

driver.get('https://github.com/login')

WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.NAME,
                                           'login'))) \
        .send_keys('Eliot.Aldersson05.09@gmail.com')

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.NAME,
                                           'password'))) \
    .send_keys('Fsociety0509')

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.NAME, 'commit'.replace(
                                               ' ', '.')))) \
    .click()

time.sleep(20)
driver.quit()