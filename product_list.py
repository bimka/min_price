from posixpath import split
from unicodedata import category
import requests
from bs4 import BeautifulSoup

def get_products(url, store_id):
    '''Функция отправляет GET-запрос, возвращая список товаров
    ''' 
    split_url = url.split('/')
    inserts = []
    
    for i in split_url[::-1]:
        if i != 'categories':
             inserts.append(i)
        else:
            inserts.append(store_id)
            break
    inserts = inserts[::-1]         
    moditify_url = make_path(inserts)
     
    r = requests.get(
            moditify_url, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0', 
                'Accept': 'application/json, text/plain, */*', 
                'Accept-Encoding': 'gzip, deflate, br', 
                'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 
                'api-version': '3.0',
                'client-token': '7ba97b6f4049436dab90c789f946ee2f', 
                'Connection': 'keep-alive', 
                'DNT': '1', 
                'Host': 'sbermarket.ru',
                'is-storefront-ssr': 'false', 
                'Referer': 'https://sbermarket.ru/metro/c/ovoshchi-frukty-oriekhi/ovoshchi',
                'Sec-Fetch-Dest': 'empty', 
                'Sec-Fetch-Mode': 'cors', 
                'Sec-Fetch-Site': 'same-origin',
                'TE': 'trailers', 
                'Cookie': u"user-id_1.0.5_lr_lruid=pQ8AALZpUGI75zMFATpqTQA%3D; siteEntryTime=Fri%20Apr%2022%202022%2021%3A15%3A35%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); reachedTimer=1; _ga=GA1.2.911227684.1646581779; _gid=GA1.2.1644138254.1650647740; t2_sid_7588506=s1.1776265614.1650647739761.1650647742833.1.3.3; tmr_reqNum=1800; external_analytics_anonymous_id=0817e773-6e48-4f65-a0ad-f15d2dc24499; _I… _gcl_au=1.1.564503019.1650647742; pageviewCount=1; _sa=SA1.75a07a87-dc5d-46af-8c9c-ec33a83f1349.1650647742; sessionId=16506477422019342055-react-catalog; iap.uid=7cfe3701f1144c158a57a1872455490f; top100_id=t1.7588506.1263500099.1650647742827; adtech_uid=5ce49b07-2561-4b40-88e9-dc6b3e5df420%3Asbermarket.ru; sessionIdPostfix=react-catalog; tmr_lvid=3f5a5b054e48faf0aebcb729cfae9d41; tmr_lvidTS=1650647746371; tmr_detect=1%7C1650647746396; _ym_uid=1650647747340769750; _ym_d=1650647747; _ym_isad=1; _ym_visorc=b".encode('cp1252')           
            }
            )
    data = r.json()
    return data['products']    

def make_path(*args):
    '''Функция собирает url
    '''
    store_id = args[0][0]
    path_vars = '/'.join(args[0][1:])
    return f"https://sbermarket.ru/api/stores/{ store_id }/products?tid={ path_vars }&page=1&per_page=100&sort=popularity"

if __name__ == "__main__":
    url = 'https://sbermarket.ru/api/stores/10/products?tid=moloko-iaitsa-new/moloko&page=1&per_page=24&sort=popularity'
    store_id = str(1373)
    url = 'https://sbermarket.ru/globus/c/katalogh-globus/sobstviennoie-proizvodstvo/piekarnia'
    products = get_products(url, store_id)
    print(products)
