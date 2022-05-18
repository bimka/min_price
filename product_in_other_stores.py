import requests

def get(store, product):
    r = requests.get(
        f'https://sbermarket.ru/api/stores/{store}/products/{product}'.format(store, product), 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0', 
            'Accept': 'application/json, text/plain, */*', 
            'Accept-Encoding': 'gzip, deflate, br', 
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 
            'If-None-Match': 'W/"3e8b75c9459c346541afea715fda0581"',
            'Connection': 'keep-alive', 
            'DNT': '1', 
            'Host': 'sbermarket.ru',
            'Referer': 'https://sbermarket.ru',
            'Sec-Fetch-Dest': 'empty', 
            'Sec-Fetch-Mode': 'cors', 
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers',  
            'Cookie': u"user-id_1.0.5_lr_lruid=pQ8AALZpUGI75zMFATpqTQA%3D; _ga=GA1.2.911227684.1646581779; t2_sid_7588506=s1.1981152115.1652891904553.1652893491672.7.74.126.1; tmr_reqNum=2611; external_analytics_anonymous_id=0817e773-6e48-4f65-a0ad-f15d2dc24499; _ga_XVJWMHHXNJ=GS1.1.1652891903.47.1.1652893495.0; _ga_9QYWDVGJZ3=GS1.1.1652891903.47.1.1652893495.49; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19dXiJCpR5%2F5GpBC5oFQq4K5EtlQD67fZhKWfiLY6Q6qovIAPXQMEsTBnVCkM%2FmGaC3nCcef2Dxug%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX18xu…1702949238-react-catalog; _pk_ses.6.3ec0=1; pageviewCount=13; siteEntryTime=Wed%20May%2018%202022%2020%3A38%3A25%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); reachedTimer=1; _gid=GA1.2.618050686.1652891905; tmr_detect=1%7C1652893363785; _ym_isad=1; __exponea_time2__=-3600.7978780269623; _ym_visorc=b; identified_address=true; isRetailersModalReminderShown=1; _gat_UA-136687175-2=1".encode('cp1252'),

            
        }
        )
    return r.json()

if __name__ == "__main__":
    store = 12
    product = 'gazirovannyy-napitok-coca-cola-0-9-l-2fec8c5'
    prod_in_other_stores = get(store, product)
    print(prod_in_other_stores['product']['offer']['price'])


