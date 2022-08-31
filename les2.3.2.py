from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button1 = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input1.send_keys(y)

    button3 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button3.click()
    print("answer is:  ", browser.switch_to.alert.text)

finally:
    # успеваем скопировать код за 0 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()