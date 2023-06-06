import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname'].form-control")
first_name.send_keys('Alex')
last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname'].form-control")
last_name.send_keys('Abramovich')
email = browser.find_element(By.CSS_SELECTOR, "[name='email'].form-control")
email.send_keys('A.A@izi.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))

button = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
file_path = os.path.join(current_dir, 'test.txt')

#button.click()
button.send_keys(file_path)

but = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
but.click()
time.sleep(30)
browser.quit()