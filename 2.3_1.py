from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button_1 = browser.find_element(By.CLASS_NAME, "trollface")
    button_1.click()
    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(y)
    button_2 = browser.find_element(By.CLASS_NAME, "btn-primary")
    button_2.click()

finally:
    time.sleep(10)
    browser.quit()