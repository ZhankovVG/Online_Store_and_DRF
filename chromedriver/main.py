from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

try:
    driver.get('http://127.0.0.1:8000/')
    time.sleep(3)
    
    klick_login = driver.find_element(By.LINK_TEXT, 'Реєстрація').click()
    time.sleep(1)
    
    username_input = driver.find_element(By.ID, 'id_username')
    username_input.clear()
    username_input.send_keys('Vitaliy111')
    time.sleep(2)
    
    email_input = driver.find_element(By.ID, 'id_email')
    email_input.clear()
    email_input.send_keys('python.developer.v@gmail.com')
    time.sleep(2)
    
    paswword_input = driver.find_element(By.ID, 'id_password1')
    paswword_input.clear()
    paswword_input.send_keys('123456789Zxcv')
    time.sleep(2)
    
    paswword_input = driver.find_element(By.ID, 'id_password2')
    paswword_input.clear()
    paswword_input.send_keys('123456789Zxcv')
    time.sleep(2)
    
    login_button = driver.find_element(By.ID, 'btn btn-primary').click()
    time.sleep(5)
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()