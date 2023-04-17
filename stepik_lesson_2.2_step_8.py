'''
2.2 Работа с файлами, списками и js-скриптами
Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом.
Отправьте полученное число в качестве ответа для этого задания.
'''

import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys("Ivanov")
    browser.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("Ivanov@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'testik.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.ID, 'file').send_keys(file_path)  # кнопка загрузить файл
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()  # кнопка submit

    time.sleep(10)
