from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    element = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    
    element.send_keys("Tест")
    

    element = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    
    element.send_keys("Tест")
    

    element = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    
    element.send_keys("Tест")
    
 
    element = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
    
    element.send_keys("Tест")
    

    element = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
    
    element.send_keys("Tест")
    


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    
    # закрываем браузер после всех манипуляций
    browser.quit()