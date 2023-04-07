from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests


def parse(url):
    page = requests.get(url=url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code)  # смотрим ответ
    soup = BeautifulSoup(page.text, 'html.parser')  # передаем страницу в bs4
    block = soup.find_all('div', style="padding: 5px; font-size: 120%;")  # находим  контейнер с нужным классом
    with open('names.txt', 'w') as f:  # открываем файл
        for item in block:
            f.write(item.text.strip().lower().title() + '\n')  # выводим текст
