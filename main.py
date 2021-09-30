# -*- coding: utf-8 -*-
import time

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
# TODO:написать фунцию с возвратом цены и сравнивать ее вывод 

while True:
    ua = UserAgent()
    headers = {'user-agent': ua.firefox}
    url = 'https://www.rbc.ru/crypto/currency/btcusd'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    mid_price = soup.find('div', class_="chart__subtitle js-chart-value")
    old_price = mid_price.text.replace(' ', '')
    time.sleep(1)
    ua = UserAgent()
    headers = {'user-agent': ua.firefox}
    url = 'https://www.rbc.ru/crypto/currency/btcusd'
    res = requests.get(url, headers=headers)

    soup_1 = BeautifulSoup(r.text, 'lxml')
    next_mid_price = soup.find('div', class_="chart__subtitle js-chart-value")
    new_price = mid_price.text.replace(' ', '')

    result = (int(old_price[0:6]) - int(new_price[0:6]))
    if result > 1000:
        print('Колебание цены ', int(new_price[0:6]))
    else:
        print(int(new_price[0:6]))
        print('разница', result)
