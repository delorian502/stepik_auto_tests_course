import time
import math
from selenium import webdriver 
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

alert = browser.switch_to.alert
alert.accept()

x = browser.find_element(By.CSS_SELECTOR, "#input_value")
y = calc(x.text)
input_int = browser.find_element(By.CSS_SELECTOR, "#answer")
input_int.send_keys(str(y))


button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

time.sleep(30)
browser.quit()