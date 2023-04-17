'''
2.3 Работа с окнами
Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке,
нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
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
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])  # переключаемся на вторую вкладку
    time.sleep(2)
    value = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(value))
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    time.sleep(2)
