import requests


r = requests.get(
    'https://sbermarket.ru/api/stores?lat=55.76009243489459&lon=37.65333537060549&include=closest_shipping_options,labels,retailer&shipping_method=delivery', 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0', 
        'Accept': 'application/json, text/plain, */*', 
        'Accept-Encoding': 'gzip, deflate, br', 
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 
        'api-version': '3.0',
        'client-token': '7ba97b6f4049436dab90c789f946ee2f', 
        'Connection': 'keep-alive', 
        'DNT': '1', 
        #'DNT-EXTERNAL-ANALYTICS': 'true', 
        'Host': 'sbermarket.ru',
        'is-storefront-ssr': 'false', 
        'Referer': 'https://sbermarket.ru/',
        'Sec-Fetch-Dest': 'empty', 
        'Sec-Fetch-Mode': 'cors', 
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers', 
        
    }
    )
ola = r.json()
print(ola)
