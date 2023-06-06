import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.implicitly_wait(3)
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#price"),"$100"))
Book = browser.find_element(By.CSS_SELECTOR,".btn.btn-primary")
Book.click()  

x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

y = calc(x)
input_1 = browser.find_element(By.CSS_SELECTOR, '#answer')

input_1.send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, "#solve")
button.click()



time.sleep(20)
browser.quit()

