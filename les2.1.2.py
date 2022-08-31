from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    x = str(x_element.get_attribute('valuex'))
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, "input.check-input[required]")
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, 'input[value="robots"]')
    button2.click()
    button3 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
