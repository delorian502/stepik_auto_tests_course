import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)


x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
y = calc(x)
str_1 = browser.find_element(By.CSS_SELECTOR, '#answer')
browser.execute_script("return arguments[0].scrollIntoView(true);",str_1)
str_1.send_keys(y)
browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
browser.quit()






