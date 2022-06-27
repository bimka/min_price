import requests

def get_categories(CONNECTION, store_id):
    '''Функция отправляет GET-запрос, получая категории продаваемых 
       товаов в виде списка
    '''
    additional_header_fields = {
        
        #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0', 
        #'Accept': 'application/json, text/plain, */*', 
        #'Accept-Encoding': 'gzip, deflate, br', 
        #'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 
        #'api-version': '3.0',
        #'client-token': '7ba97b6f4049436dab90c789f946ee2f', 
        #'Connection': 'keep-alive', 
        #'DNT': '1', 
        #'Host': 'sbermarket.ru',
        #'is-storefront-ssr': 'false', 
        #'Referer': 'https://sbermarket.ru/',
        #'Sec-Fetch-Dest': 'empty', 
        #'Sec-Fetch-Mode': 'cors', 
        #'Sec-Fetch-Site': 'same-origin',
        #'TE': 'trailers',   
    }
    
    response = CONNECTION.get(
        f'https://sbermarket.ru/api/stores/{ store_id }/categories?depth=2&include='.format(store_id), 
        headers = CONNECTION.headers,
        )
    data = response.json()
    return data['categories']

if __name__ == "__main__":
    store_id = 21
    sb_markets = get_categories(store_id)
    print(sb_markets[0])