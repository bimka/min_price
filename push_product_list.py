import requests
import json

def send(legacy_product_id, market, store_id):
    '''Функция отправляет POST-запрос с id товара для отображения его 
       в корзине Сбермаркета
    ''' 
    
    cookies = {
        'user-id_1.0.5_lr_lruid': 'pQ8AAEtvq2KUTEGEAScUbgA%3D',
        'siteEntryTime': 'Mon%20Jun%2020%202022%2021%3A07%3A05%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)',
        'reachedTimer': '1',
        '_pk_id.6.3ec0': '554ea64efeb09509.1655744836.',
        '_pk_ses.6.3ec0': '1',
        '_ga': 'GA1.2.911227684.1646581779',
        '_gid': 'GA1.2.450740361.1655744836',
        'tmr_reqNum': '7119',
        't3_sid_7588506': 's1.1508004786.1655744836079.1655746645135.1.12.12.1',
        'external_analytics_anonymous_id': 'e77741c7-101c-4ce3-89e6-9672b6d3d15c',
        '_808db7ba1248': '%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1655746616%7D%2C%7B%22source%22%3A%22localhost%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1655746627%7D%5D',
        '_Instamart_session': 'Yy96NHlJVkpQWW9rRjV2cEw5MUE0TGNseGZ1S3Y4VXEydWwyT242VVVhK09ESFNzZWsySXBOREM5eG0zOExzeGVjZHYxWUJOZkVBQVVSN1E4L2tWclRlUDdjODZVSGp4N0lCMFZSNVF4dSthU0l2U2hXNDVIOUFVWFZSbGY4MTN3VWhoVUFxbGRFd2svL0lzVUYxUkxSZ1l4dTFoQU9xNXBFeWN0ZTRuVTZIc3p2ejRac1N6Z3czODdzallnOGc5Zm9tRDhMSjZwZXIwb1RvbHlzZndVdz09LS1qOWhIWVFPSG82bDlWUkhwOHorbkxRPT0%3D--ef9914f5a4a70802847d3c54364606970216439e',
        'city_info': '%7B%22slug%22%3A%22izhevsk%22%2C%22name%22%3A%22%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%22%2C%22lat%22%3A56.8489%2C%22lon%22%3A53.2316%7D',
        '_ga_XVJWMHHXNJ': 'GS1.1.1655738243.9.1.1655746632.0',
        '_ga_9QYWDVGJZ3': 'GS1.1.1655738243.9.1.1655746632.32',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2FNfby6o%2FVVMzvnsQdyVYbVocq9888k7LGFWrqyqW0aftw%2ByJkecNH20%2FxtQ%2BDrdJYMx9dF2dvpng%3D%3D',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2FRlMTjQWCyiG2jvRN37jftB79X8AcfLL4%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19P05%2BsnUgPSZO2Pqiawo8arOokQ576WTM%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2BQfTUAsLLV7kUa9UyezytxxFjC2S7czg0Murv2o21PhIvM7zKqbgD%2BiHfJsGT5d818tnu9uVbe%2BA8DUvnsX%2FRuHRa9qF20XjyrS5IujCWsUjKUBFYRnRsPZFcG6xCe6RL%2BYi4OrM6YWC9f%2Fh2EAak%2BtkzuzfyNNExDwQHa1uFr6lwFHnvKlvM9',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B9yuBTLG0UsJU%2FZMefrN1rbN8%2FNZrQSME%3D',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2FKdXu5pA%2BryJh0BQYehzfpFJCm0h2P1Tw%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX1%2FFEyNea4NRp8PtYox3lgsTnkljhzJb%2BYk%3D',
        '_gcl_au': '1.1.273329989.1655744838',
        'pageviewCount': '5',
        '_sa': 'SA1.7cf2ea6d-fc4a-43b8-b1bd-78cfed959923.1655744838',
        'sessionId': '16557448382169947988',
        'iap.uid': '8cc0dca2376242bd87e532ac6e36c899',
        'rrpvid': '31',
        'last_visit': '1655732233023%3A%3A1655746633023',
        'adtech_uid': '837acbcb-7d08-4931-86fe-6113250a96dc%3Asbermarket.ru',
        'top100_id': 't1.7588506.2075659749.1655744838991',
        'tmr_lvid': '134ecddd7fa0098a247d5739a2d0b35c',
        'tmr_lvidTS': '1655744840094',
        '_ym_uid': '1655744840682950050',
        '_ym_d': '1655744840',
        'tmr_detect': '1%7C1655746634439',
        '_ym_isad': '1',
        'rcuid': '62b0a945e1779400018a46b9',
        '_ym_visorc': 'b',
        'identified_address': 'true',
        '__exponea_etc__': '1e014acc-e2a4-4f6e-a949-82860d83326f',
        '__exponea_time2__': '-3.713731527328491',
        '_gat_UA-136687175-2': '1',
        'rrbasket': '',
    }
    """
    cookies = {
        'user-id_1.0.5_lr_lruid': 'pQ8AAEtvq2KUTEGEAScUbgA%3D',
        'siteEntryTime': 'Mon%20Jun%2020%202022%2021%3A07%3A05%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)',
        'reachedTimer': '0',
        '_pk_id.6.3ec0': '554ea64efeb09509.1655744836.',
        '_pk_ses.6.3ec0': '1',
        '_ga': 'GA1.2.911227684.1646581779',
        '_gid': 'GA1.2.450740361.1655744836',
        '_gat_UA-136687175-2': '1',
        'tmr_reqNum': '7080',
        't3_sid_7588506': 's1.1508004786.1655744836079.1655744838998.1.2.2.1',
        'external_analytics_anonymous_id': 'e77741c7-101c-4ce3-89e6-9672b6d3d15c',
        '_808db7ba1248': '%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1655744834%7D%5D',
        '_Instamart_session': 'Q2l2NnVqRE1UcTlSTmphaENybEd5U1lpb3g4ZzFZa2dES1FZL3I0R0JzYkpVRjNvcENNam9oU0g4L3ZjVzVGUUdQell0ZVJxSnR4aGR2SU1jWHBRVzFPQmliWXo3aGVPdlZJQjhYVXNXa3NuN0E2bi9GelNKZ04rUS9EenNreVU4ZWtFd2Mrc1o4cVRkN0xZNGM2Znh1bTlLenZLRVdCakp3SGh0QWlObWFxSkl5TWxiYk8zdXlxZnBRbUNyS2RjLS1LQ2pEUUc4L1d2MEc5OWY3NjBkRjVnPT0%3D--846005a0d8cdefe43ac52c264ba9432f7160b24e',
        #'city_info': '%7B%22slug%22%3A%22izhevsk%22%2C%22name%22%3A%22%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%22%2C%22lat%22%3A56.8489%2C%22lon%22%3A53.2316%7D',
        '_ga_XVJWMHHXNJ': 'GS1.1.1655738243.9.1.1655744838.0',
        '_ga_9QYWDVGJZ3': 'GS1.1.1655738243.9.1.1655744838.59',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2FDwRqkNAomON8FqojMmOLN87jwRsBtRCCAyhzFjP74b8DTGdr0tiSSrmLTrIy8J4RGKlfDgIiypA%3D%3D',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2FOeqpUnICw7eNc6mohcRz%2F2hSCiQ%2ByIrg%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19vBoarYXMyEhfZt3DgCBQC8kbzu6r6NW4%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2BtiVPfuuSLIqSunFD%2FKmfxghhBZ3BXIYPqWJ4b7BRUseWi4cogdmmdNXS6fRDYiSQCwSGftusLHU9Y3c%2F6zoNoZheGUAuXfMkOBPMFjEPupOhSIf5m0yxazyWVzm%2Bd0wPWDuVsTBXQVGpt9n%2FLce2mxVkxC2jv4WQv0c%2BnJBfKz%2FXfnp6Y2kng',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B18kxjuKZ4Hzgb5VNx6aLqpIkDBilX29Q%3D',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2FKdXu5pA%2BryJh0BQYehzfpFJCm0h2P1Tw%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX1%2FFEyNea4NRp8PtYox3lgsTnkljhzJb%2BYk%3D',
        '_gcl_au': '1.1.273329989.1655744838',
        'pageviewCount': '1',
        '_sa': 'SA1.7cf2ea6d-fc4a-43b8-b1bd-78cfed959923.1655744838',
        'sessionId': '16557448382169947988',
        'iap.uid': '8cc0dca2376242bd87e532ac6e36c899',
        'rrpvid': '31',
        'last_visit': '1655730438988%3A%3A1655744838988',
        'adtech_uid': '837acbcb-7d08-4931-86fe-6113250a96dc%3Asbermarket.ru',
        'top100_id': 't1.7588506.2075659749.1655744838991',
        'tmr_lvid': '134ecddd7fa0098a247d5739a2d0b35c',
        'tmr_lvidTS': '1655744840094',
        '_ym_uid': '1655744840682950050',
        '_ym_d': '1655744840',
        'tmr_detect': '1%7C1655744840739',
        '_ym_isad': '1',
        'rcuid': '62b0a945e1779400018a46b9',
        '_gat_%5Bobject%20Object%5D': '1',
        '_ym_visorc': 'b',

        #### дополнительные значения
        '__exponea_etc__': '15d49727-5ba4-42f3-ac28-c93e1948a892',
        '_pk_ref.6.3ec0': '%5B%22%22%2C%22%22%2C1655738242%2C%22https%3A%2F%2Flocalhost%3A8080%2F%22%5D',
        '__exponea_time2__': '-2.5507009029388428',
        'identified_address': 'true', # попробовать изменить на false
        'rrbasket': '',
        'hide_pre_replacement_bubble': 'true',
    }
    """
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': f'https://sbermarket.ru/{ market }?sid={ store_id }',
    'Content-Type': 'application/json;charset=utf-8',
    'X-CSRF-Token': '2C6sq9Dflgb5V2jGnLssFSrrJQkjIsnJV1AtPVEr0yALx6atYUh6ZO1YrjXyXVJPiM13SXp8RDCR9JmFA8ZU3g==',
    'Origin': 'https://sbermarket.ru',
    'DNT': '1',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'user-id_1.0.5_lr_lruid=pQ8AAEtvq2KUTEGEAScUbgA%3D; siteEntryTime=Mon%20Jun%2020%202022%2021%3A07%3A05%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); reachedTimer=1; _pk_id.6.3ec0=554ea64efeb09509.1655744836.; _pk_ses.6.3ec0=1; _ga=GA1.2.911227684.1646581779; _gid=GA1.2.450740361.1655744836; tmr_reqNum=7119; t3_sid_7588506=s1.1508004786.1655744836079.1655746645135.1.12.12.1; external_analytics_anonymous_id=e77741c7-101c-4ce3-89e6-9672b6d3d15c; _808db7ba1248=%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1655746616%7D%2C%7B%22source%22%3A%22localhost%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1655746627%7D%5D; _Instamart_session=Yy96NHlJVkpQWW9rRjV2cEw5MUE0TGNseGZ1S3Y4VXEydWwyT242VVVhK09ESFNzZWsySXBOREM5eG0zOExzeGVjZHYxWUJOZkVBQVVSN1E4L2tWclRlUDdjODZVSGp4N0lCMFZSNVF4dSthU0l2U2hXNDVIOUFVWFZSbGY4MTN3VWhoVUFxbGRFd2svL0lzVUYxUkxSZ1l4dTFoQU9xNXBFeWN0ZTRuVTZIc3p2ejRac1N6Z3czODdzallnOGc5Zm9tRDhMSjZwZXIwb1RvbHlzZndVdz09LS1qOWhIWVFPSG82bDlWUkhwOHorbkxRPT0%3D--ef9914f5a4a70802847d3c54364606970216439e; city_info=%7B%22slug%22%3A%22izhevsk%22%2C%22name%22%3A%22%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%22%2C%22lat%22%3A56.8489%2C%22lon%22%3A53.2316%7D; _ga_XVJWMHHXNJ=GS1.1.1655738243.9.1.1655746632.0; _ga_9QYWDVGJZ3=GS1.1.1655738243.9.1.1655746632.32; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FNfby6o%2FVVMzvnsQdyVYbVocq9888k7LGFWrqyqW0aftw%2ByJkecNH20%2FxtQ%2BDrdJYMx9dF2dvpng%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FRlMTjQWCyiG2jvRN37jftB79X8AcfLL4%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19P05%2BsnUgPSZO2Pqiawo8arOokQ576WTM%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BQfTUAsLLV7kUa9UyezytxxFjC2S7czg0Murv2o21PhIvM7zKqbgD%2BiHfJsGT5d818tnu9uVbe%2BA8DUvnsX%2FRuHRa9qF20XjyrS5IujCWsUjKUBFYRnRsPZFcG6xCe6RL%2BYi4OrM6YWC9f%2Fh2EAak%2BtkzuzfyNNExDwQHa1uFr6lwFHnvKlvM9; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B9yuBTLG0UsJU%2FZMefrN1rbN8%2FNZrQSME%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FKdXu5pA%2BryJh0BQYehzfpFJCm0h2P1Tw%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2FFEyNea4NRp8PtYox3lgsTnkljhzJb%2BYk%3D; _gcl_au=1.1.273329989.1655744838; pageviewCount=5; _sa=SA1.7cf2ea6d-fc4a-43b8-b1bd-78cfed959923.1655744838; sessionId=16557448382169947988; iap.uid=8cc0dca2376242bd87e532ac6e36c899; rrpvid=31; last_visit=1655732233023%3A%3A1655746633023; adtech_uid=837acbcb-7d08-4931-86fe-6113250a96dc%3Asbermarket.ru; top100_id=t1.7588506.2075659749.1655744838991; tmr_lvid=134ecddd7fa0098a247d5739a2d0b35c; tmr_lvidTS=1655744840094; _ym_uid=1655744840682950050; _ym_d=1655744840; tmr_detect=1%7C1655746634439; _ym_isad=1; rcuid=62b0a945e1779400018a46b9; _ym_visorc=b; identified_address=true; __exponea_etc__=1e014acc-e2a4-4f6e-a949-82860d83326f; __exponea_time2__=-3.713731527328491; _gat_UA-136687175-2=1; rrbasket=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
    }
    
    for product in legacy_product_id:        
        jsonProductConversion = json.dumps({"line_item":{"offer_id" : product}})
        print(jsonProductConversion)
        r = requests.post(
                          'https://sbermarket.ru/api/line_items', 
                          cookies=cookies, 
                          headers=headers, 
                          data=jsonProductConversion,
                         )
        print(r.text)



if __name__ == "__main__":
    legacy_product_id = ["12680662"]
    market = 'metro'
    store_id = '21'
    products = send(legacy_product_id, market, store_id)
    print(products)
