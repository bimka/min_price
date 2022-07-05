import requests
from fake_useragent import UserAgent

def establish_connection():
    ''' Функция отправляет на сервер Сбермаркета запрос для 
         coздания сессии  и получения куки
    '''
    url = 'https://sbermarket.ru/'

    session = requests.Session()

    user_agent = UserAgent()
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0', 
        'User-Agent': user_agent.random,
    }

    """headers = {
        'authority': 'sbermarket.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'User-Agent': user_agent.random,
    }"""
    
    session.headers.update(headers)

    session.get(        
        url,
        #headers=headers,
        )
    session.get(        
        "https://api-sbermarket.exponea.com/js/exponea.min.js"
        )
    add_cookies(session)
    add_csrf_token_to_headers(session)
    #session.cookies.clear()
    print(session.cookies)
    return session


def add_cookies(session):
    '''Функция отправляет запрос на сервер Сбермаркета для получения куки
    '''
    urls = [
        
        

        ["GET", "https://sbermarket.ru/_next/static/chunks/main-178ed2f92e226848.js"],

    ]

    #print(session.cookies)
    #print(session.headers)
    for url in urls:
        try:
            session.get(        
                url[1],
                )
        except:
            session.post(        
                url[1],
                )

    #print(session.cookies)



    

def add_csrf_token_to_headers(session):
    '''Функция отправляет запрос на сервер Сбермаркета для получения 
       csrf-токена
    '''
    url = 'https://sbermarket.ru/api/next/page_part/browser_head'

    additional_header_fields = {
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

    session.headers.update(additional_header_fields)

    responce = session.get(
        url, 
        )
        
    csrf_token = responce.json()
    session.headers.update(csrf_token)

if __name__ == "__main__":
    session = establish_connection()
    #print(session.cookies)