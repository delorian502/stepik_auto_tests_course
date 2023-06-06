import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    

    
    
    n1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    
    n2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    sum_1 = int(n1.text)+int(n2.text)
    print(sum_1)
    
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    
    select.select_by_value(str(sum_1))
    
    
 
    y = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    y.click()
    
    
    

finally:
    # успеваем скопировать код за 30 секунд
    
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла