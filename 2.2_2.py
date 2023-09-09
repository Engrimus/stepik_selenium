from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input_1 = browser.find_element(By.NAME, 'firstname')
    input_1.send_keys('Ivan')
    input_2 = browser.find_element(By.NAME, 'lastname')
    input_2.send_keys('Dirkov')
    input_3 = browser.find_element(By.NAME, 'email')
    input_3.send_keys('pigeon')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Тестовый.txt"
    file_path = os.path.join(current_dir, file_name)
    button_1 = browser.find_element(By.ID, "file")
    button_1.send_keys(file_path)
    button_2 = browser.find_element(By.CLASS_NAME, "btn-primary")
    button_2.click()
finally:
    time.sleep(10)
    browser.quit()