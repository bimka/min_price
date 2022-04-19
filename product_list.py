import requests
from bs4 import BeautifulSoup

def get_products(url):
    '''Функция отправляет GET-запрос, возвращая список товаров
    '''
    r = requests.get(
        url, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0', 
            'Accept': 'application/json, text/plain, */*', 
            'Accept-Encoding': 'gzip, deflate, br', 
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 
            'api-version': '3.0',
            'client-token': '7ba97b6f4049436dab90c789f946ee2f', 
            'Connection': 'keep-alive', 
            'DNT': '1', 
            'Host': 'sbermarket.ru',
            'is-storefront-ssr': 'false', 
            'Referer': 'https://sbermarket.ru/',
            'Sec-Fetch-Dest': 'empty', 
            'Sec-Fetch-Mode': 'cors', 
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers', 
            
        }
        )
    soup = BeautifulSoup(r.text, 'html.parser')
    body = soup.find_all("ul", class_="ProductsGrid_styles_grid__zigKP")
    return body

if __name__ == "__main__":
    url = 'https://sbermarket.ru/categories/moloko-iaitsa-new/moloko'
    products = get_products(url)
    print(products)
 
 