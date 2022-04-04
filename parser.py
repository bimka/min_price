import requests
from bs4 import BeautifulSoup
import json

# Создами класс с магазинами

class Market:
    def __init__(self, name, logo, url):
        self.name = name
        self.logo = logo
        self.url = url


r = requests.get('https://sbermarket.ru/')
soup = BeautifulSoup(r.text, 'html.parser')


markets = soup.find_all(class_='h9K7R')
ola = markets[0]
print(ola)
# for market in markets:
#     market_name = market.img.get('alt')
#     market_logo = market.find(class_ = 'l4AA8 _2ccKV').get('src')
#     print(market_name, market_logo)
#     obj = Market(name = market.img.get('alt'), 
#                 logo = market.find(class_ = 'l4AA8 _2ccKV').get('src'), 
#                 url = )



if __name__ == '__main__':
    metro = Market('Metro', "metro_logo.jpg", 'merto.ru')
    print(metro.name, metro.url)



