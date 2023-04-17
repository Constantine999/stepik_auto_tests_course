'''
2.2 Работа с файлами, списками и js-скриптами
Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов.
Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
Отправьте полученное число в качестве ответа для этого задания.

Когда ваш код заработает, попробуйте запустить его на странице https://suninjuly.github.io/selects2.html.
Ваш код и для нее тоже должен пройти успешно.
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/selects1.html")

    value = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(value))
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

    time.sleep(5)
