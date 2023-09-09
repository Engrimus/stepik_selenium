from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button = browser.find_element(By.ID, "book")
    button.click()
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(y)
    button_2 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)
    button_2.click()

finally:
    time.sleep(10)
    browser.quit() #Не забыть закрыть браузер, чтобы память не утекала