import time 
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
int_1 = browser.find_element(By.CSS_SELECTOR, "#input_value").text
y = calc(int_1)
input_1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input_1.send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

time.sleep(30)
browser.quit()


