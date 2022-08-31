import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome()



try:

    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    input1.send_keys('firstname')
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    input2.send_keys('firstname')
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    input3.send_keys('firstname')


    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test1.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button3 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
