import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# открываем браузер и переходим на сайт Google
browser = webdriver.Chrome()
browser.get('https://www.google.com/')
time.sleep(5)


# проверяем наличие логотипа Google на главной странице
logo = browser.find_element_by_id('hplogo')
assert logo.is_displayed()
time.sleep(5)
# проверяем наличие разделов поиска: Веб, Картинки, Видео, Новости, Карты, Музыка
search_options = browser.find_elements_by_css_selector('div.hdtb-mitem a')
expected_options = ['Веб', 'Картинки', 'Видео', 'Новости', 'Карты', 'Музыка']
actual_options = [option.text for option in search_options]
assert actual_options == expected_options
time.sleep(5)
# проверяем работоспособность кнопок "Поиск в Google" и "Мне повезет!"
search_box = browser.find_element_by_name('q')
search_box.send_keys('test')
search_box.send_keys(Keys.RETURN)
assert 'test' in browser.title
browser.back()
lucky_button = browser.find_element_by_css_selector('div.FPdoLc button[name="btnI"]')
lucky_button.click()
assert 'test' in browser.title
time.sleep(5)
# проверяем наличие ссылок на другие продукты Google: Gmail, Диск, Календарь, Переводчик, YouTube
google_apps = browser.find_elements_by_css_selector('a.gb_g')
expected_apps = ['Gmail', 'Диск', 'Календарь', 'Переводчик', 'YouTube']
actual_apps = [app.text for app in google_apps]
assert actual_apps == expected_apps
time.sleep(5)
# проверяем работоспособность ссылок на социальные сети: Facebook, Twitter, Instagram
social_links = browser.find_elements_by_css_selector('div.FPdoLc a')
for link in social_links:
    if 'Facebook' in link.get_attribute('href'):
        link.click()
        break
browser.switch_to.window(browser.window_handles[1])
assert 'Facebook' in browser.title
browser.close()
browser.switch_to.window(browser.window_handles[0])
for link in social_links:
    if 'Twitter' in link.get_attribute('href'):
        link.click()
        break
browser.switch_to.window(browser.window_handles[1])
assert 'Twitter' in browser.title
browser.close()
browser.switch_to.window(browser.window_handles[0])
for link in social_links:
    if 'Instagram' in link.get_attribute('href'):
        link.click()
        break
browser.switch_to.window(browser.window_handles[1])
assert 'Instagram' in browser.title
browser.close()
browser.switch_to.window(browser.window_handles[0])
time.sleep(5)

# проверяем работоспособность ссылки на Google Play для загрузки приложений
play_link = browser.find_element_by_css_selector('a[href="https://play.google.com/store"]')
play_link.click()
assert 'Google Play' in browser.title
browser.back()
time.sleep(5)

# проверяем наличие ссылок на услуги Google: Реклама, Бизнес-решения, Наука и образование
services = browser.find_elements_by_css_selector('div._Gs a')
expected_services = ['Реклама', 'Бизнес-решения', 'Наука и образование']
actual_services = [service.text for service in services]
assert actual_services == expected_services
time.sleep(5)

# проверяем наличие ссылок на языковые версии Google для других стран и регионов
language_links = browser.find_elements_by_css_selector('div.hfgbLd a')
for link in language_links:
    link.click()
    assert 'Google' in browser.title
    browser.back()
time.sleep(5)

# проверяем работоспособность кнопки "Настройки" для персонализации поисковых запросов
settings_button = browser.find_element_by_css_selector('a[href="https://www.google.com/preferences"]')
settings_button.click()
assert 'Настройки' in browser.title
browser.back()
time.sleep(5)

# проверяем работоспособность кнопки "Язык" для выбора языка интерфейса сайта
language_button = browser.find_element_by_css_selector('a[href="https://www.google.com/setprefs?sig=0_5YrVJW2Nz8h6sQrG0D1P4sZ9m3c%3D&hl=en&source=homepage&sa=X&ved=0ahUKEwiq9JvH5MvzAhXKuHEKHQk7BvMQ2ZgBCAU"]')
language_button.click()
language_options = browser.find_elements_by_css_selector('div.O4YeWd div ul li')
time.sleep(5)
for option in language_options:
    if 'Español' in option.text:
        option.click()
        break
time.sleep(5)
assert 'Google' in browser.title

# закрываем браузер
browser.quit()