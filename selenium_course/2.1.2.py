import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    

    
    
    x_element = browser.find_element(By.CSS_SELECTOR, ".form-group .nowrap#input_value" )
    x = x_element.text
    y = calc(x)

    ans_w = browser.find_element(By.CSS_SELECTOR, "#answer")
    ans_w.send_keys(y)
    
    c_b = browser.find_element(By.CSS_SELECTOR, ".form-check-input#robotCheckbox")
    c_b.click()
    
    
    r_b = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    r_b.click()
    

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла