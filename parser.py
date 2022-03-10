import requests
from bs4 import BeautifulSoup
import json

# Надо сериализировать информацию по магазинам и засунуть в json

r = requests.get('https://sbermarket.ru/')
soup = BeautifulSoup(r.text, 'html.parser')


markets = soup.find_all(class_='h9K7R')
data = ''
for market in markets:
    market_name = market.img.get('alt')
    market_logo = market.find(class_ = 'l4AA8 _2ccKV').get('src')
    print(market_name, market_logo)

"""for market in markets:
    print(market)"""
market_logo = markets[0].find(class_ = 'l4AA8 _2ccKV')
print(market_logo.get('src'))

"""
market
logo


"""



