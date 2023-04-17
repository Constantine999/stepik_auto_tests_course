'''
2.3 Работа с окнами
Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
Отправьте полученное число в качестве ответа на это задание.
'''

import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()  # кнопка submit
    confirm = browser.switch_to.alert
    confirm.accept()
    value = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(value))
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    time.sleep(5)
