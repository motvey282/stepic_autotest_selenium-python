from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    button = browser.find_element(By.CSS_SELECTOR, '#book').click()

    x1 = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x1)
    input1 = browser.find_element(By.CSS_SELECTOR, '.form-control')
    input1.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, '#solve').click()

    print("answer is:  ", browser.switch_to.alert.text)
finally:
    time.sleep(1)

    browser.quit()