from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


browser = webdriver.Chrome()


try:

    browser.get("http://suninjuly.github.io/selects2.html")

    num1 = browser.find_element(By.CSS_SELECTOR, 'span#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, 'span#num2').text
    sum1 = str(int(num1)+int(num2))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum1)
    button3 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
