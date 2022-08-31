from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser.get("http://SunInJuly.github.io/execute_script.html")
    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input1.send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    button1 = browser.find_element(By.CSS_SELECTOR, "input.form-check-input[required]")
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
