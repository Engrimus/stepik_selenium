from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value').text
    y = calc(int(x_element))
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button_1 = browser.find_element(By.ID, "robotCheckbox")
    button_1.click()
    button_2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)
    button_2.click()
    button_3 = browser.find_element(By.CLASS_NAME, "btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_3)
    button_3.click()
finally:
    time.sleep(10)
    browser.quit()