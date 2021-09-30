# -*- coding: latin-1 -*-
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
headers = {'user-agent': ua.firefox}
url = 'https://www.google.com/search?client=firefox-b-d&q=wtyf+%2Cbnrjbyf'
r = requests.get(url, headers=headers, )

soup = BeautifulSoup(r.text, 'lxml')

mid_price = soup.find_all(['div', 'span'], "r0bn4c rQMQod")
for i in mid_price:
    if '+' in i.text:
        print(i.text)

