import requests

def send(lat, lon):
    ''' Функция отправляет на сервер Сбермаркета координаты доставки
    '''
                
    cookies = {
        'siteEntryTime': 'Mon%20Jun%2020%202022%2020%3A18%3A24%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)',
        'reachedTimer': '1',
        'user-id_1.0.5_lr_lruid': 'pQ8AAEtvq2KUTEGEAScUbgA%3D',
        '_ga': 'GA1.2.911227684.1646581779',
        '_gid': 'GA1.2.93653872.1655741909',
        'tmr_reqNum': '7031',
        't3_sid_7588506': 's1.333181926.1655741908543.1655742053953.1.7.7.1',
        'external_analytics_anonymous_id': '1f6428d4-a2d9-41de-a1a4-5761ca9e7d60',
        '_808db7ba1248': '%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1655742011%7D%2C%7B%22source%22%3A%22sbermarket.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1655742049%7D%5D',
        '_Instamart_session': 'Yzhrb2hNa3JCSkRtangyRUVoOXJvVm1Qc3BWd1dCNVdBTjJKUmNtdkZoTGRKRkwzV0VxNklPNjZCcVNLT09heGFGcml0dWpFaGNVd1F0UThTZHpDWTV1ZmN3Rkd0OFRINXVRYTJzd2p2a1duTzlpU0V4MHZld2VMTGdBREdqVGpCa2N4OFBGcTZNSEhCVTA5RVZ5d21nSTQybXY5WHdzSWxrL3FiK0JaTUFZNTc2M3VIWXZvYlZZZ2dlZ0gxYXVTbXd4bkZKQ0NJRnhVOG55dkg1T3l3dz09LS0wSFdBcUdtcDFpUTVsWFNRTVlVV1FRPT0%3D--5b4b65b85e57074f6d3a663a2149ef0466ef7810',
        'city_info': '%7B%22slug%22%3A%22izhevsk%22%2C%22name%22%3A%22%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%22%2C%22lat%22%3A56.8489%2C%22lon%22%3A53.2316%7D',
        '_ga_XVJWMHHXNJ': 'GS1.1.1655738243.9.1.1655742053.0',
        '_ga_9QYWDVGJZ3': 'GS1.1.1655738243.9.1.1655742053.3',
        '_pk_id.6.3ec0': 'c37b9f940ba7d43f.1655741911.',
        '_pk_ses.6.3ec0': '1',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2Bebi6Lu6ONXMTeQv2Ck5IFAdZYHnWLVfYzJn7VFHu0uHFE%2FSWM0kk450c1VK%2F%2FjxIGW9ZSVwS%2BUg%3D%3D',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX19aW6FPnQvUPwvopJC1sa5oYq6eYPtO9B0%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19C3sBqkUDaASOeP%2F0UQXu1ea78%2Fnrwmp8%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX18sFIY%2Fbu8DUy8sl99K7hiZqbxHJiCXxaxAZiHKedyRI%2F4pog9KPTGH7t3QvceaOlRWGY80N0tGnEdemUyHbTezHuCuZgmp%2FT4FQbbY0ipl0OPPzn62eCLRp5zluZk1ZeSy5xKpyd3Tyh5pfDh2DGDvYVPFPXcGOjpdpIWXzxksmg8uBf5Kl2Az',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B%2FAWAUxbGlAn0YbWRYza9gXxbZyPk6RgA%3D',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2BZkejMQdD3UZAJ5MzlF9qDOtOm534dO5U%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX1%2FFXwClSEi2QfsonSVDLoRVyhryYQHx0EE%3D',
        '_gcl_au': '1.1.624209716.1655741912',
        'pageviewCount': '4',
        '_sa': 'SA1.38cefb70-0cd0-4e01-bf5c-cb5fa446e073.1655741911',
        'sessionId': '16557419118755821910',
        'iap.uid': 'de6c82afd50b4d188ef97c86d4ea342b',
        'last_visit': '1655727653945%3A%3A1655742053945',
        'adtech_uid': 'd3cc2c6b-9b3e-4194-80e8-2e597fd44b8d%3Asbermarket.ru',
        'top100_id': 't1.7588506.341787136.1655741912305',
        'rrpvid': '115',
        'tmr_lvid': 'cf690a8c4b6d386f859875c5aa3c1e59',
        'tmr_lvidTS': '1655741913747',
        'tmr_detect': '1%7C1655742054988',
        'rcuid': '62b09dd6b7ea52000160906b',
        '__exponea_etc__': '9b2d1cd7-5409-4135-bf36-472dcc2461b6',
        '__exponea_time2__': '-2.1862258911132812',
        '_ym_uid': '1655741914388571830',
        '_ym_d': '1655741914',
        '_ym_isad': '1',
        '_ym_visorc': 'b',
        'cookies_consented': 'yes',
        'identified_address': 'true',
        '_gat_%5Bobject%20Object%5D': '1',
        'rr-testCookie': 'testvalue',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://sbermarket.ru/metro?sid=12',
        'DNT': '1',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'siteEntryTime=Mon%20Jun%2020%202022%2020%3A18%3A24%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); reachedTimer=1; user-id_1.0.5_lr_lruid=pQ8AAEtvq2KUTEGEAScUbgA%3D; _ga=GA1.2.911227684.1646581779; _gid=GA1.2.93653872.1655741909; tmr_reqNum=7031; t3_sid_7588506=s1.333181926.1655741908543.1655742053953.1.7.7.1; external_analytics_anonymous_id=1f6428d4-a2d9-41de-a1a4-5761ca9e7d60; _808db7ba1248=%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1655742011%7D%2C%7B%22source%22%3A%22sbermarket.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1655742049%7D%5D; _Instamart_session=Yzhrb2hNa3JCSkRtangyRUVoOXJvVm1Qc3BWd1dCNVdBTjJKUmNtdkZoTGRKRkwzV0VxNklPNjZCcVNLT09heGFGcml0dWpFaGNVd1F0UThTZHpDWTV1ZmN3Rkd0OFRINXVRYTJzd2p2a1duTzlpU0V4MHZld2VMTGdBREdqVGpCa2N4OFBGcTZNSEhCVTA5RVZ5d21nSTQybXY5WHdzSWxrL3FiK0JaTUFZNTc2M3VIWXZvYlZZZ2dlZ0gxYXVTbXd4bkZKQ0NJRnhVOG55dkg1T3l3dz09LS0wSFdBcUdtcDFpUTVsWFNRTVlVV1FRPT0%3D--5b4b65b85e57074f6d3a663a2149ef0466ef7810; city_info=%7B%22slug%22%3A%22izhevsk%22%2C%22name%22%3A%22%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%22%2C%22lat%22%3A56.8489%2C%22lon%22%3A53.2316%7D; _ga_XVJWMHHXNJ=GS1.1.1655738243.9.1.1655742053.0; _ga_9QYWDVGJZ3=GS1.1.1655738243.9.1.1655742053.3; _pk_id.6.3ec0=c37b9f940ba7d43f.1655741911.; _pk_ses.6.3ec0=1; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2Bebi6Lu6ONXMTeQv2Ck5IFAdZYHnWLVfYzJn7VFHu0uHFE%2FSWM0kk450c1VK%2F%2FjxIGW9ZSVwS%2BUg%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX19aW6FPnQvUPwvopJC1sa5oYq6eYPtO9B0%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19C3sBqkUDaASOeP%2F0UQXu1ea78%2Fnrwmp8%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX18sFIY%2Fbu8DUy8sl99K7hiZqbxHJiCXxaxAZiHKedyRI%2F4pog9KPTGH7t3QvceaOlRWGY80N0tGnEdemUyHbTezHuCuZgmp%2FT4FQbbY0ipl0OPPzn62eCLRp5zluZk1ZeSy5xKpyd3Tyh5pfDh2DGDvYVPFPXcGOjpdpIWXzxksmg8uBf5Kl2Az; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B%2FAWAUxbGlAn0YbWRYza9gXxbZyPk6RgA%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BZkejMQdD3UZAJ5MzlF9qDOtOm534dO5U%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2FFXwClSEi2QfsonSVDLoRVyhryYQHx0EE%3D; _gcl_au=1.1.624209716.1655741912; pageviewCount=4; _sa=SA1.38cefb70-0cd0-4e01-bf5c-cb5fa446e073.1655741911; sessionId=16557419118755821910; iap.uid=de6c82afd50b4d188ef97c86d4ea342b; last_visit=1655727653945%3A%3A1655742053945; adtech_uid=d3cc2c6b-9b3e-4194-80e8-2e597fd44b8d%3Asbermarket.ru; top100_id=t1.7588506.341787136.1655741912305; rrpvid=115; tmr_lvid=cf690a8c4b6d386f859875c5aa3c1e59; tmr_lvidTS=1655741913747; tmr_detect=1%7C1655742054988; rcuid=62b09dd6b7ea52000160906b; __exponea_etc__=9b2d1cd7-5409-4135-bf36-472dcc2461b6; __exponea_time2__=-2.1862258911132812; _ym_uid=1655741914388571830; _ym_d=1655741914; _ym_isad=1; _ym_visorc=b; cookies_consented=yes; identified_address=true; _gat_%5Bobject%20Object%5D=1; rr-testCookie=testvalue',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'If-None-Match': 'W/42553194a2e5c680817165bf57ba7e2e',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'cargo': 'false',
        'lat': lat,
        'lon': lon,
    }

    response = requests.get(
        'https://sbermarket.ru/api/stores/12/next_deliveries', 
        params=params, 
        cookies=cookies, 
        headers=headers)  

    return response.text

if __name__ == "__main__":
    lat = 55.760286020319455
    lon = 37.64037493664552
    user_coord = send(lat, lon)
    print(user_coord)
