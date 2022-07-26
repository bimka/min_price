import requests
import json

def send(CONNECTION, legacy_product_id, market, store_id):
    '''Функция отправляет POST-запрос с id товара для отображения его 
       в корзине Сбермаркета
    ''' 
    updated_header_field = {
        "X-CSRF-Token": CONNECTION.headers["csrf_token"],
        'Referer': f'https://sbermarket.ru/{ market }?sid={ store_id }',
        "Content-Type": "application/json;charset=utf-8", 
        "Origin": "https://sbermarket.ru", 
        'Upgrade-Insecure-Requests': None,
        'csrf_param': None, 
        'api-version': None, 
        'client-token': None, 
        'is-storefront-ssr': None,
        'csrf_token': None,
        'Host': None,
    }

    
    cookies = {
        'user-id_1.0.5_lr_lruid': 'pQ8AAEtvq2KUTEGEAScUbgA%3D',
        'tmr_reqNum': '7917',
        't3_sid_7588506': 's1.248075399.1656859198435.1656859472854.3.19.23.1',
                'external_analytics_anonymous_id': '1c55a303-8853-40bb-a925-150843ea7adf',
        '_808db7ba1248': '%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1656825898%7D%2C%7B%22source%22%3A%22localhost%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1656859469%7D%2C%7B%22source%22%3A%22sbermarket.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1656859457%7D%5D',
                '_Instamart_session': 'MEpwREtleG1wNmRBckxUSjdSWUhzb0hpQnVCS0VnWWllbGRCYTRoTHRYU2hOQ01neG1mNXQ5NVkvcDZFaG92UlZYNDIva0grQk02WnlyWGRLRS9wdkt5NXZEeUQzMEJSNEpaL2pVUTYyd3c1RjIyYkRQaEtRT3lLaEhiWjRwUDJxRmJOSUdkelZBMGxmOURET1pyaWdPQmZubk5jNjBsbHovM2xnZXlnNWVqMzJIZHJ5K1Noa1NnSERJdC9rUVZ5M2s2UTFyd1haMSs4K3dHc09aWS9tdz09LS1WWjVBUm50Y3ZXcjYzb3B5NGxFUFp3PT0%3D--8de8c5a69060266870f2e0bb8e7f0b21c1d14f42',
        'city_info': '%7B%22slug%22%3A%22izhevsk%22%2C%22name%22%3A%22%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%22%2C%22lat%22%3A56.8489%2C%22lon%22%3A53.2316%7D',
        '_pk_id.6.3ec0': '2e48812dae79b80d.1656825900.',
        '_sa': 'SA1.fbd80660-a583-40f5-bbc7-c6065ec90654.1656825900',
        'iap.uid': '38692b0461c64a0d81a029516ab00acb',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX19lvzripVUGKPVc8tDblI19OGJrBHeNzZAtiRp0eJcbPPGlwlU7TMlmOphOzJG3evkbOp3KKDh96A%3D%3D',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2FP9HPjbEcg%2BDkloBvZ73o5OWqD%2ByLQ9JE%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19jqbQsaBJ%2B1gF4qMilYG9x7a8ucKGLHBg%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B%2BcGGpaZC5HvW9yXAQFiBFfkre%2BP5voBszBtA2kok02vQWN58OrsbbCx7Y5wVXrPL0qavZhgqYplHKupcNafO3twevu5jPLAZU2hrIt2KZWPwzmatzgVYMAqYmRukag%2F7nLEvHOPCBA5%2BBXvEei19OI2AZ07hMB4XPoqLF2a8%2FeKMIL5Dr16O%2BMj8jm%2B1h99nx8DZSHTW7UAFj9aXb87KzVzxXfRHTF%2FjA%2B5NB13sZkMItqfwi8UsKtTgBuHim%2BSsSNMRa4M8ubg%3D%3D',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B8iM7eRtt%2FgfmQFp1XmXgddHew85NaH%2F0%3D',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX19gqpS%2Fw8rH3cSFNw2307RDOc%2FzkzxAHsg%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX19PC2KOvor6ElQhr0outedCKGPm7lwMMT8%3D',
        'last_visit': '1656845072847%3A%3A1656859472847',
        'adtech_uid': 'd4a6b42b-0830-4b35-b390-f656321f49fe%3Asbermarket.ru',
        'top100_id': 't1.7588506.315424029.1656825900804',
        'rrpvid': '739965285446456',
        'rcuid': '62c1282cb7ea520001b555c2',
        '__exponea_etc__': '8ffe2fbe-c8d7-49ea-82a8-c39e36178d3b',
        'tmr_lvid': '6634f365fccffb2c323fa1bc4da16622',
        'tmr_lvidTS': '1656825903404',
        '_ym_uid': '165682590482438678',
        '_ym_d': '1656825904',
        'tmr_detect': '1%7C1656859475880',
        '_ym_isad': '1',
        '_pk_ref.6.3ec0': '%5B%22%22%2C%22%22%2C1656859197%2C%22https%3A%2F%2Flocalhost%3A8080%2F%22%5D',
        '_pk_ses.6.3ec0': '1',
        'sessionId': '16568591969286749169',
        '__exponea_time2__': '-1.5426337718963623',
        '_ym_visorc': 'b',
        'identified_address': 'true',
    }

    add_cookies = {
        'user-id_1.0.5_lr_lruid': 'pQ8AAEtvq2KUTEGEAScUbgA%3D',
        'tmr_reqNum': '7917',
        't3_sid_7588506': 's1.248075399.1656859198435.1656859472854.3.19.23.1',
        '_pk_id.6.3ec0': '2e48812dae79b80d.1656825900.',
        '_sa': 'SA1.fbd80660-a583-40f5-bbc7-c6065ec90654.1656825900',
        'iap.uid': '38692b0461c64a0d81a029516ab00acb',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX19lvzripVUGKPVc8tDblI19OGJrBHeNzZAtiRp0eJcbPPGlwlU7TMlmOphOzJG3evkbOp3KKDh96A%3D%3D',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2FP9HPjbEcg%2BDkloBvZ73o5OWqD%2ByLQ9JE%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19jqbQsaBJ%2B1gF4qMilYG9x7a8ucKGLHBg%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B%2BcGGpaZC5HvW9yXAQFiBFfkre%2BP5voBszBtA2kok02vQWN58OrsbbCx7Y5wVXrPL0qavZhgqYplHKupcNafO3twevu5jPLAZU2hrIt2KZWPwzmatzgVYMAqYmRukag%2F7nLEvHOPCBA5%2BBXvEei19OI2AZ07hMB4XPoqLF2a8%2FeKMIL5Dr16O%2BMj8jm%2B1h99nx8DZSHTW7UAFj9aXb87KzVzxXfRHTF%2FjA%2B5NB13sZkMItqfwi8UsKtTgBuHim%2BSsSNMRa4M8ubg%3D%3D',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B8iM7eRtt%2FgfmQFp1XmXgddHew85NaH%2F0%3D',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX19gqpS%2Fw8rH3cSFNw2307RDOc%2FzkzxAHsg%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX19PC2KOvor6ElQhr0outedCKGPm7lwMMT8%3D',
        'last_visit': '1656845072847%3A%3A1656859472847',
        'adtech_uid': 'd4a6b42b-0830-4b35-b390-f656321f49fe%3Asbermarket.ru',
        'top100_id': 't1.7588506.315424029.1656825900804',
        'rrpvid': '739965285446456',
        'rcuid': '62c1282cb7ea520001b555c2',
        '__exponea_etc__': '8ffe2fbe-c8d7-49ea-82a8-c39e36178d3b',
        'tmr_lvid': '6634f365fccffb2c323fa1bc4da16622',
        'tmr_lvidTS': '1656825903404',
        '_ym_uid': '165682590482438678',
        '_ym_d': '1656825904',
        'tmr_detect': '1%7C1656859475880',
        '_ym_isad': '1',
        '_pk_ref.6.3ec0': '%5B%22%22%2C%22%22%2C1656859197%2C%22https%3A%2F%2Flocalhost%3A8080%2F%22%5D',
        '_pk_ses.6.3ec0': '1',
        'sessionId': '16568591969286749169',
        '__exponea_time2__': '-1.5426337718963623',
        '_ym_visorc': 'b',
        'identified_address': 'true',
        'city_info': '%7B%22slug%22%3A%22izhevsk%22%2C%22name%22%3A%22%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%22%2C%22lat%22%3A56.8489%2C%22lon%22%3A53.2316%7D',
        #'_Instamart_session': 'MEpwREtleG1wNmRBckxUSjdSWUhzb0hpQnVCS0VnWWllbGRCYTRoTHRYU2hOQ01neG1mNXQ5NVkvcDZFaG92UlZYNDIva0grQk02WnlyWGRLRS9wdkt5NXZEeUQzMEJSNEpaL2pVUTYyd3c1RjIyYkRQaEtRT3lLaEhiWjRwUDJxRmJOSUdkelZBMGxmOURET1pyaWdPQmZubk5jNjBsbHovM2xnZXlnNWVqMzJIZHJ5K1Noa1NnSERJdC9rUVZ5M2s2UTFyd1haMSs4K3dHc09aWS9tdz09LS1WWjVBUm50Y3ZXcjYzb3B5NGxFUFp3PT0%3D--8de8c5a69060266870f2e0bb8e7f0b21c1d14f42',
        '_808db7ba1248': '%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1656825898%7D%2C%7B%22source%22%3A%22localhost%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1656859469%7D%2C%7B%22source%22%3A%22sbermarket.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1656859457%7D%5D',
        'external_analytics_anonymous_id': '1c55a303-8853-40bb-a925-150843ea7adf',
    }

    CONNECTION.headers.update(updated_header_field)   
    CONNECTION.cookies.update(add_cookies)  

    #print(CONNECTION.headers)
    #print(CONNECTION.cookies)
    
    cookies = {
        'external_analytics_anonymous_id': 'a2867bab-b47c-4ef7-a038-2699750889fb',
        'city_info': '%7B%22slug%22%3A%22izhevsk%22%2C%22name%22%3A%22%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%22%2C%22lat%22%3A56.8489%2C%22lon%22%3A53.2316%7D',
        'sessionId': '16570389005511649156',
        '_pk_id.6.3ec0': '6666b909a4273444.1657038901.',
        '_pk_ses.6.3ec0': '1',
        '_sa': 'SA1.77ac8a8c-8315-442b-bf01-643fb226cab9.1657038900',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2BYTtKaRzdkzjd7DTpC3JZMDyN13Qt4wrs%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX1%2FKlSvRrXBl97jwEQowkQkznS48EZSLxN0%3D',
        'iap.uid': 'f4b096eaee80403b8c3fd1c07a339d5a',
        '__exponea_etc__': '1804dc4a-522d-4f8f-88ca-8e8c8aa28f8d',
        '__exponea_time2__': '-1.1302967071533203',
        '_ym_uid': '1657038902171200132',
        '_ym_d': '1657038902',
        'tmr_lvid': '142609c24b888882bef91da70f2a7e1b',
        'tmr_lvidTS': '1657038902076',
        'adtech_uid': 'e7245bed-0b8c-41a4-871c-6e3d72a266b8%3Asbermarket.ru',
        'top100_id': 't1.7588506.589713232.1657038902183',
        'user-id_1.0.5_lr_lruid': 'pQ8AADZoxGJEAQufAeVv4AA%3D',
        '_ym_isad': '1',
        'rrpvid': '227818853636169',
        'rcuid': '62c46835b7ea5200016062eb',
        '_ym_visorc': 'b',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX1%2BvW4MzyPZNy7PCKkwB%2FEBS7YRBGayw10k%3D',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX19H20nCu9aA4HeUP1AyK3v03kGGVOzz%2Fto%3D',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX19IxLuVwX52fW59%2Fq5tMy%2BLage4oBRc36UvYtLDfFWSXPKCFnOccFh%2FqRJ%2BGM0T%2FOHfhRN43TD6Ww%3D%3D',
        '_808db7ba1248': '%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1657038918%7D%2C%7B%22source%22%3A%22sbermarket.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1657038914%7D%5D',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2BZUlKgVMlk42v5uRknfuYdTQG5BPibqsY%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX19gTXGfWNH8TZjr72AhUKq2GVU9SM1VLjzjTKToY0j2%2FhzObL8%2BzU0%2Biz4A0ISVVkoM3NgMkag6U5Mg5VZ0WezfVADiYqMhXIiWstH4g2m0wYaf2nXzsq1dqAXzTKHiwGeLbGH0Fe5aHIkTsoTRAcE%2B%2FeI4DGOsW1o%2Fb8hCDiRIUeO2pYT16AWF8qMnFxp4iMnIEvZyuRYL0SWtrDu1XKu3AoRPGchREaBjn%2Fd%2FsKrsxNkz3noohdNrzEGUYe0G8g1X399p8ADqKfuBs8xGHubrtDl%2F1Z6ecae3Ew8tIUKMm9nZGOLD%2Btq9FJGB%2B3FvV9ANgY9bZUPVLg%3D%3D',
        'identified_address': 'true',
        '_Instamart_session': 'Yk5KMWhDNjQ3a3lRa1FPNmxPWlZMWmZGc2xrZDNNV3pXUmRpREQ5UzU2MVpxOXFDbHJzTy9wZ0FRbHE0RHNFQzJpcVAza3NMQ0lDa0dRR2NWWXdYSk5Va3JPYngvaHp2VmZYZm53SlRPUlRrZlZXQlBJb3RJSWFwd1RUTXlya1V5dFp0aEU4V1NERk9XelYvQ1NoN1pvQk9XWkpEWkJxbXowN0l3dERLSFJrUU52RlR3bDNMa3ozYWlpMkc2M3R1SStNUUQ1a2F2eUJkUkNwUWU1NEpyZz09LS1ybnRQcUxFc0JhNlZUS3Q1bjk4ajNBPT0%3D--5e0c5e17397435211c6b5f4721b70e36308d571e',
        'rr-testCookie': 'testvalue',
        'last_visit': '1657024522916%3A%3A1657038922916',
        't3_sid_7588506': 's1.108285170.1657038902187.1657038922939.1.3.3.1',
        'tmr_detect': '1%7C1657038923065',
        'tmr_reqNum': '14',
    }

    headers = {
        'authority': 'sbermarket.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',

        'origin': 'https://sbermarket.ru',
        'referer': 'https://sbermarket.ru/metro?sid=21',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-csrf-token': 'Nal7VCeiy38reUcyqanBrUolysVntrZ1lbXb/TmDthqSfwmdQJAu6EconROVE4DmCMQfNsPnREz/edrBdYPqzA==',
    }

    for product in legacy_product_id:
        line_item = {"line_item": {"offer_id": product}}
        json_line_item = json.dumps(line_item)
        """response = CONNECTION.post(
                          'https://sbermarket.ru/api/line_items', 
                          data = json_line_item,
                         )"""
        response = requests.post(
                          'https://sbermarket.ru/api/line_items', 
                          data = json_line_item,
                          cookies=cookies, 
                          headers=headers,
                         )
        print(response.text)



if __name__ == "__main__":
    legacy_product_id = ["12680662"]
    market = 'metro'
    store_id = '21'
    products = send(legacy_product_id, market, store_id)
    print(products)
