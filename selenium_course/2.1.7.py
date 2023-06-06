import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    

    
    
    img_1 = browser.find_element(By.CSS_SELECTOR, "#treasure")
    intt = img_1.get_attribute("valuex")
    print(intt)
    y = calc(intt)
    text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
    text_area.send_keys(y)
    c_b = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    c_b.click()
    r_b = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    r_b.click()
    button_1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button_1.click()
    
    
    

finally:
    # успеваем скопировать код за 30 секунд
    
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла