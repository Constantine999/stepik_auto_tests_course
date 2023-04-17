'''
2.1 Основные методы Selenium

Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
Продолжим использовать силу роботов 🤖 для решения повседневных задач.
На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера,
но сложным для человека.

Ваша программа должна выполнить следующие шаги:
Открыть страницу https://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
'''

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/math.html")
    value = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(value))

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

    time.sleep(10)
