import requests
import json

def send(legacy_product_id, market, store_id):
    '''Функция отправляет POST-запрос с id товара для отображения его 
       в корзине Сбермаркета
    ''' 
    
    cookies = {
        'user-id_1.0.5_lr_lruid': 'pQ8AAEtvq2KUTEGEAScUbgA%3D',
        '_ga': 'GA1.2.911227684.1646581779',
        'tmr_reqNum': '6379',
        't3_sid_7588506': 's1.219645830.1655647999218.1655649786623.5.22.238.1',
        '_ga_XVJWMHHXNJ': 'GS1.1.1655647999.8.1.1655649523.0',
        '_ga_9QYWDVGJZ3': 'GS1.1.1655647999.8.1.1655649523.40',
        'external_analytics_anonymous_id': '5acd5713-aa20-4ac0-afed-b1cf7a275c98',
        '_808db7ba1248': '%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1655649508%7D%2C%7B%22source%22%3A%22ru.stackoverflow.com%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1655402611%7D%2C%7B%22source%22%3A%22localhost%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1655649519%7D%2C%7B%22source%22%3A%22sbermarket.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1655642308%7D%5D',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2FHwfC9wZvLXpoivcGLfrv76kzYqTVBJHOdV5qtthgMRMfoDShMpd9ybSCTDq%2F1QtmDTW64QivmqQ%3D%3D',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2BP3THAblGWLaL10gDIGzeoZKfIxIcyQlc%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19oJl7tw%2BGrJYtlBCXWdXoYIomZcbRmuv4%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B75h7RqM7IUz%2BT5NRQRDySm3N%2FamOjiUY4wH%2FMmJMYQrsK9fxa6YitPhXFZdR%2FnunCq51rUQMQn2LehExTzi8ROqsv7EL504a7oxtsVCoi0NkZRWwRIeY9X48e9p5OEK2qn7dF3OQJxGNgzn%2Fi2W5CN7%2BBamjL83nDyrYH6susF7JWNgXXFxqJ',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B2FZ7iPLZrTSzH6B3f062VkyUPVPt3OfY%3D',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2BmI4V5Oeu1i56PAzc7RAb8yt70WSiv0NY%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX1%2BylEPuxT797%2B9H3qaXGwVQfjKO8Szmw%2Fk%3D',
        '_gcl_au': '1.1.1360594403.1655402313',
        '_sa': 'SA1.6ffb0faa-ad27-4469-bb2b-d40ff01e4a74.1655402313',
        '_pk_id.6.3ec0': '4a1130da217a271b.1655402313.',
        'iap.uid': '79d63f9b0b3542428876501a0301957b',
        'rrpvid': '129',
        'last_visit': '1655635123901%3A%3A1655649523901',
        'adtech_uid': 'dda2487a-abe3-4737-a894-dd583ca812f1%3Asbermarket.ru',
        'top100_id': 't1.7588506.1788315731.1655402315007',
        'tmr_lvid': 'fa1f0e30c6e25808a4cafe704ebb6c25',
        'tmr_lvidTS': '1655402316726',
        '_ym_uid': '1655402317469774869',
        '_ym_d': '1655402317',
        'rcuid': '62ab6f4ab7ea52000131c1e3',
        '__exponea_etc__': '15d49727-5ba4-42f3-ac28-c93e1948a892',
        '_pk_ref.6.3ec0': '%5B%22%22%2C%22%22%2C1655648005%2C%22https%3A%2F%2Flocalhost%3A8080%2F%22%5D',
        '_gid': 'GA1.2.152941237.1655565615',
        'tmr_detect': '1%7C1655649524877',
        'siteEntryTime': 'Sun%20Jun%2019%202022%2015%3A19%3A37%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)',
        '__exponea_time2__': '-2.851045846939087',
        '_ym_isad': '1',
        '_Instamart_session': 'aXJEZ1hRYnJLV1lYbFFzUkpjRTg3ZmRVWWZQSVRtZkExNFBGWjh6bUF0NUlIQkU2WkROWGFWZEFQcVZuY2dBejR0dTlNSW91OHpucEVvbnZKRHByRGVXUHkwc1BJVFBjM295QzZUVjdQdEg5Smh2Ni80WWlKYWlYRDBIU3JXMGF2dVZkQUNPRUNCYWlBc29FVXlWTXJhbWxZZjU5QU9vS2hHaGVUK244OHJOdWFWVEVOT2JxMlJsdkRZV3VrZDAwcVkyaHhUSHE2clF3U082N1E3dVF6dz09LS0vRjJlUUttNWdHL1MyMFJmclVhK3RnPT0%3D--7077896784bb9b1d128ef468c157c6886f8eae80',
        'city_info': '%7B%22slug%22%3A%22izhevsk%22%2C%22name%22%3A%22%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%22%2C%22lat%22%3A56.8489%2C%22lon%22%3A53.2316%7D',
        'pageviewCount': '27',
        'identified_address': 'true',
        '_pk_ses.6.3ec0': '1',
        'sessionId': '16556480055695859695',
        '_ym_visorc': 'b',
        'reachedTimer': '1',
        'user_is_adult': 'true',
        'rrbasket': '',
        '_gat_UA-136687175-2': '1',
        }

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': f'https://sbermarket.ru/{ market }?sid={ store_id }',
    'Content-Type': 'application/json;charset=utf-8',
    'X-CSRF-Token': 'M+CwdDInEKskEymG7yLQXhfcGXrXreXcHBavGPEsrrTCMS0rWS4zdBAM+EJq8LViYuGi5/KIr74pwL7uFybBgw==',
    'Origin': 'https://sbermarket.ru',
    'DNT': '1',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'user-id_1.0.5_lr_lruid=pQ8AAEtvq2KUTEGEAScUbgA%3D; _ga=GA1.2.911227684.1646581779; tmr_reqNum=6379; t3_sid_7588506=s1.219645830.1655647999218.1655649786623.5.22.238.1; _ga_XVJWMHHXNJ=GS1.1.1655647999.8.1.1655649523.0; _ga_9QYWDVGJZ3=GS1.1.1655647999.8.1.1655649523.40; external_analytics_anonymous_id=5acd5713-aa20-4ac0-afed-b1cf7a275c98; _808db7ba1248=%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1655649508%7D%2C%7B%22source%22%3A%22ru.stackoverflow.com%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1655402611%7D%2C%7B%22source%22%3A%22localhost%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1655649519%7D%2C%7B%22source%22%3A%22sbermarket.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1655642308%7D%5D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FHwfC9wZvLXpoivcGLfrv76kzYqTVBJHOdV5qtthgMRMfoDShMpd9ybSCTDq%2F1QtmDTW64QivmqQ%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BP3THAblGWLaL10gDIGzeoZKfIxIcyQlc%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19oJl7tw%2BGrJYtlBCXWdXoYIomZcbRmuv4%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B75h7RqM7IUz%2BT5NRQRDySm3N%2FamOjiUY4wH%2FMmJMYQrsK9fxa6YitPhXFZdR%2FnunCq51rUQMQn2LehExTzi8ROqsv7EL504a7oxtsVCoi0NkZRWwRIeY9X48e9p5OEK2qn7dF3OQJxGNgzn%2Fi2W5CN7%2BBamjL83nDyrYH6susF7JWNgXXFxqJ; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B2FZ7iPLZrTSzH6B3f062VkyUPVPt3OfY%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BmI4V5Oeu1i56PAzc7RAb8yt70WSiv0NY%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2BylEPuxT797%2B9H3qaXGwVQfjKO8Szmw%2Fk%3D; _gcl_au=1.1.1360594403.1655402313; _sa=SA1.6ffb0faa-ad27-4469-bb2b-d40ff01e4a74.1655402313; _pk_id.6.3ec0=4a1130da217a271b.1655402313.; iap.uid=79d63f9b0b3542428876501a0301957b; rrpvid=129; last_visit=1655635123901%3A%3A1655649523901; adtech_uid=dda2487a-abe3-4737-a894-dd583ca812f1%3Asbermarket.ru; top100_id=t1.7588506.1788315731.1655402315007; tmr_lvid=fa1f0e30c6e25808a4cafe704ebb6c25; tmr_lvidTS=1655402316726; _ym_uid=1655402317469774869; _ym_d=1655402317; rcuid=62ab6f4ab7ea52000131c1e3; __exponea_etc__=15d49727-5ba4-42f3-ac28-c93e1948a892; _pk_ref.6.3ec0=%5B%22%22%2C%22%22%2C1655648005%2C%22https%3A%2F%2Flocalhost%3A8080%2F%22%5D; _gid=GA1.2.152941237.1655565615; tmr_detect=1%7C1655649524877; siteEntryTime=Sun%20Jun%2019%202022%2015%3A19%3A37%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); __exponea_time2__=-2.851045846939087; _ym_isad=1; _Instamart_session=aXJEZ1hRYnJLV1lYbFFzUkpjRTg3ZmRVWWZQSVRtZkExNFBGWjh6bUF0NUlIQkU2WkROWGFWZEFQcVZuY2dBejR0dTlNSW91OHpucEVvbnZKRHByRGVXUHkwc1BJVFBjM295QzZUVjdQdEg5Smh2Ni80WWlKYWlYRDBIU3JXMGF2dVZkQUNPRUNCYWlBc29FVXlWTXJhbWxZZjU5QU9vS2hHaGVUK244OHJOdWFWVEVOT2JxMlJsdkRZV3VrZDAwcVkyaHhUSHE2clF3U082N1E3dVF6dz09LS0vRjJlUUttNWdHL1MyMFJmclVhK3RnPT0%3D--7077896784bb9b1d128ef468c157c6886f8eae80; city_info=%7B%22slug%22%3A%22izhevsk%22%2C%22name%22%3A%22%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%22%2C%22lat%22%3A56.8489%2C%22lon%22%3A53.2316%7D; pageviewCount=27; identified_address=true; _pk_ses.6.3ec0=1; sessionId=16556480055695859695; _ym_visorc=b; reachedTimer=1; user_is_adult=true; rrbasket=; _gat_UA-136687175-2=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
    }
    
    line_items = []
    ola = []
    
    for product in legacy_product_id:
        
        line_items.append(json.dumps({"line_item":{"offer_id" : product}}))
    for i in line_items:
        print(i)
        r = requests.post(
                            'https://sbermarket.ru/api/line_items', 
                            cookies=cookies, 
                            headers=headers, 
                            data=i,
                            )
        ola.append(r.text)
    print(ola)



if __name__ == "__main__":
    legacy_product_id = "12680662"
    market = 'metro'
    store_id = '21'
    products = send(legacy_product_id, market, store_id)
    print(products)
