import requests
import fake_useragent

def get_cookies():
    ''' Функция отправляет на сервер Сбермаркета запрос для 
         coздания сессии  и получения куки
    '''
    url = 'https://sbermarket.ru/'

    session = requests.Session()

    user = fake_useragent.UserAgent().random

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': user,
    }
    
    responce = session.get(        
        url,
        headers = headers,
        )
        
    add_csrf_token_to_cookies(session)

def add_csrf_token_to_cookies(session):
    '''Функция отправляет запрос на сервер Сбермаркета для получения 
       csrf-токена
    '''
    url = 'https://sbermarket.ru/api/next/page_part/browser_head'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://sbermarket.ru/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers',
    }

    session.headers.update(headers)

    responce = session.get(
        url, 
        )
        
    csrf_token = responce.json()
    session.headers.update(csrf_token)

if __name__ == "__main__":
    session = get_cookies()
    print(session)
    
