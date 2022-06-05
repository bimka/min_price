import requests
import json

def send(offer_id, market, store_id):
    '''Функция отправляет POST-запрос с id товара для отображения его 
       в корзине Сбермаркета
    ''' 
    offer_id = offer_id
    cookies = {
        'user-id_1.0.5_lr_lruid': 'pQ8AALZpUGI75zMFATpqTQA%3D',
        '_ga': 'GA1.2.911227684.1646581779',
        'tmr_reqNum': '2998',
        'external_analytics_anonymous_id': '0817e773-6e48-4f65-a0ad-f15d2dc24499',
        '_ga_XVJWMHHXNJ': 'GS1.1.1654083880.63.1.1654083887.0',
        '_ga_9QYWDVGJZ3': 'GS1.1.1654083881.63.1.1654083887.54',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2BijQwsUuBVPnMrHbwUJR8Xd9Nxi8oizEF%2Baje7OJ9kEs2ec7BUmpVrDYHGuR73GUAEkKC5ERhtKg%3D%3D',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2BXiAk4QiYLKRUm8EG4ChyMmb5oURqmSOQG2miC1e6WtmA5IzrPxkY4CXstHtf9IR%2Fx3WP4gaf0vg%3D%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19ke6ToqthP9G8VHUFxbfW%2F%2FtpVDVXyX8s%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX18tK8xenw8evb9XXXxVeaEdFyyYs7jNCnaFvtFs8KXgD0Bww0G7dWDgbqf%2Fod89l0ROMqEx1%2BODeMTEckiMDCvGkS6Y2Zyx88YatL9AAlG1JoB6zeFsiEOUbwAdSYYbq53C9%2FaCQWnEpv5HV%2Bv7vYK8gj0Oj%2FZDxpcxNI5pKrrqeYAfif4XUmsdDoaoScz0GdueI24dbCgqPNzZfOjrFR%2F5MqGM3Ay0Zic0BOiFu%2FNytDCpQBlp7LhAlF0tVwzbVe7QQZEB3ePrfhne0aHN6WUOQd65MdG9MMqOiZq5b92LZxM36QgjvaPe1N7SBeP%2F3TCTqX8ZiWlqL6w1pzr84I6jjcbzhQ52OeQvfDBnstZrb%2FxBaNibyL7LAFWL3ZO2YD2s6%2B5vOacvz0DB5cx71t05kZjPsIjtj9nab9eovemMM8tbDCUSJ16OcmzxKyJpJef%2B991IJfazYH0xMRiVcCjVfCpEfFc4kRP%2FCkr8ZTMD%2F6cppBJ%2FVbbqk%2BgSKbXCcjcyZmqG%2B4Q%2BXBrW4rBbhzgy42xaLfTi2lnJtCZ67VI1lAWUespgGFvBspwR5l7AeKii85C1svbzvrm3uiEmXPs74%2BRmYZnPaK%2BxnR%2FK06KSdLYIWrrAt76xVxSQcP33yEY6gy%2BHSqROLjomFwH4j4%2B8By2UdlCpyKmBMoNJlU4N5uwzN8mZgGtkyHFVPhiOGag0cEHzifi3KuavuUVrb0wxHkNH4rhL4SsQ%2B3%2FJOEjDz3X1QdX4xzXBVtw59YgNMVZ6O4%2Fcx0VPHG41m527bU9yNcv98AxhB5apClu8wM%2FRmptgATY9qO7S2UY2hmbTGsdXTdTuwYDUBVF1UdtY%2BzQWUc32Aq8QzQ4%3D',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B0w7gB0ss2%2FLsu0tKeoNSrcBYBXxBtLn0%3D',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1873GasXShvY75ASIc2%2FXAAsXJYJVZVq7w%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX18yOFqvU3nMFPJL31BiiABVGbJgLz2Q3fg%3D',
        '_gcl_au': '1.1.564503019.1650647742',
        '_sa': 'SA1.75a07a87-dc5d-46af-8c9c-ec33a83f1349.1650647742',
        'iap.uid': '7cfe3701f1144c158a57a1872455490f',
        'adtech_uid': '5ce49b07-2561-4b40-88e9-dc6b3e5df420%3Asbermarket.ru',
        'sessionIdPostfix': 'react-catalog',
        'tmr_lvid': '3f5a5b054e48faf0aebcb729cfae9d41',
        'tmr_lvidTS': '1650647746371',
        '_ym_uid': '1650647747340769750',
        '_ym_d': '1650647747',
        '__exponea_etc__': '82b7ee4e-9dbd-4cdf-ba59-a8929283b0c0',
        '_pk_id.6.3ec0': 'e1909fc2c9a6ab6f.1650904577.',
        'rrpvid': '97',
        'rcuid': '6292520e82847c0001a4fcda',
        'resemble_b2b_tag': 'true',
        'remember_user_token': 'BAhbCFsGaQP39%2B5JIhl5UmV6R05nTGUzUmpfNGphaW1LTgY6BkVGSSIXMTY1Mzc1NjYzMC4yNDEwNzMxBjsARg%3D%3D--11b06e255cf99ae28bedd4ce55d34541a61042f8',
        '_808db7ba1248': '%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1654080270%7D%2C%7B%22source%22%3A%22sbermarket.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1654080278%7D%5D',
        '_gid': 'GA1.2.87396216.1653927888',
        'tmr_detect': '1%7C1654083890871',
        'hide_pre_replacement_bubble': 'true',
        '_ym_isad': '1',
        '_Instamart_session': 'WTl0a3pMcUV1OE5QY2FHOWFkdUFuSGZCQ2sraVdnSENLWEY0SWVGRVhKYnIyeHpjN1VzRnFqZmw3UngwQ3JjSzQveHJ5dERaR3NMVVU2SzFleVdOcTg4Smlja1VDcHZwNkQ2eHc2c0dlaWxvWllPR0U0VHlsRTZwQm11YlNzS29LcCs5L3FxeXdHOWRkVFVxV0VIL2Q5YzJCTVpzb25qRG53dEJGTGFaMVZ3cFRNSy9HMlFGbGhYVk81eHJsUTBIVStFY0Zib2xwMkhnYlVMaFJ5TG5uMzVNVktETzRLZzdoTkJpTm52d3pXbXduU1NBNGI4MUwxNEhOSUlzUkUxaEJHVTB5SHJNQTJQY1lkcDVhMFprbkgwL0UycTRWcS9ZQVgySFhrcFdLMms9LS1lcHVtOFlRNlJWMGxIeEFmdnhMUXRBPT0%3D--4214d590553490b298516c54e4d59cf493eba22b',
        'city_info': '%7B%22slug%22%3A%22perm%22%2C%22name%22%3A%22%D0%9F%D0%B5%D1%80%D0%BC%D1%8C%22%2C%22lat%22%3A58.0041%2C%22lon%22%3A56.2397%7D',
        '_pk_ses.6.3ec0': '1',
        'pageviewCount': '2',
        'sessionId': '16540838798648561069-react-catalog',
        'top100_id': 't1.7588506.1490529896.1654083881398',
        't2_sid_7588506': 's1.1318650359.1654083881400.1654083887965.1.3.3.1',
        'siteEntryTime': 'Wed%20Jun%2001%202022%2015%3A44%3A42%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)',
        'reachedTimer': '0',
        '_gat_UA-136687175-2': '1',
        'identified_address': 'true',
        'identified_user': 'true',
        '_ym_visorc': 'w',
        '_gat_%5Bobject%20Object%5D': '1',
        '__exponea_time2__': '-3607.4388065338135',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': f'https://sbermarket.ru/{ market }?sid={ store_id }'.format(),
        'Content-Type': 'application/json;charset=utf-8',
        'X-CSRF-Token': 'm+KvXOKhqQQIm81eWN/fMPD6amsKIz5BJjA6CpiJY5jzgWWzg/w5n2fYaONKr5wegu9nAxnajhVpMU5GiuqpUA==',
        'Origin': 'https://sbermarket.ru',
        'DNT': '1',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        'Cookie': 'user-id_1.0.5_lr_lruid=pQ8AALZpUGI75zMFATpqTQA%3D; _ga=GA1.2.911227684.1646581779; tmr_reqNum=2998; external_analytics_anonymous_id=0817e773-6e48-4f65-a0ad-f15d2dc24499; _ga_XVJWMHHXNJ=GS1.1.1654083880.63.1.1654083887.0; _ga_9QYWDVGJZ3=GS1.1.1654083881.63.1.1654083887.54; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2BijQwsUuBVPnMrHbwUJR8Xd9Nxi8oizEF%2Baje7OJ9kEs2ec7BUmpVrDYHGuR73GUAEkKC5ERhtKg%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BXiAk4QiYLKRUm8EG4ChyMmb5oURqmSOQG2miC1e6WtmA5IzrPxkY4CXstHtf9IR%2Fx3WP4gaf0vg%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19ke6ToqthP9G8VHUFxbfW%2F%2FtpVDVXyX8s%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX18tK8xenw8evb9XXXxVeaEdFyyYs7jNCnaFvtFs8KXgD0Bww0G7dWDgbqf%2Fod89l0ROMqEx1%2BODeMTEckiMDCvGkS6Y2Zyx88YatL9AAlG1JoB6zeFsiEOUbwAdSYYbq53C9%2FaCQWnEpv5HV%2Bv7vYK8gj0Oj%2FZDxpcxNI5pKrrqeYAfif4XUmsdDoaoScz0GdueI24dbCgqPNzZfOjrFR%2F5MqGM3Ay0Zic0BOiFu%2FNytDCpQBlp7LhAlF0tVwzbVe7QQZEB3ePrfhne0aHN6WUOQd65MdG9MMqOiZq5b92LZxM36QgjvaPe1N7SBeP%2F3TCTqX8ZiWlqL6w1pzr84I6jjcbzhQ52OeQvfDBnstZrb%2FxBaNibyL7LAFWL3ZO2YD2s6%2B5vOacvz0DB5cx71t05kZjPsIjtj9nab9eovemMM8tbDCUSJ16OcmzxKyJpJef%2B991IJfazYH0xMRiVcCjVfCpEfFc4kRP%2FCkr8ZTMD%2F6cppBJ%2FVbbqk%2BgSKbXCcjcyZmqG%2B4Q%2BXBrW4rBbhzgy42xaLfTi2lnJtCZ67VI1lAWUespgGFvBspwR5l7AeKii85C1svbzvrm3uiEmXPs74%2BRmYZnPaK%2BxnR%2FK06KSdLYIWrrAt76xVxSQcP33yEY6gy%2BHSqROLjomFwH4j4%2B8By2UdlCpyKmBMoNJlU4N5uwzN8mZgGtkyHFVPhiOGag0cEHzifi3KuavuUVrb0wxHkNH4rhL4SsQ%2B3%2FJOEjDz3X1QdX4xzXBVtw59YgNMVZ6O4%2Fcx0VPHG41m527bU9yNcv98AxhB5apClu8wM%2FRmptgATY9qO7S2UY2hmbTGsdXTdTuwYDUBVF1UdtY%2BzQWUc32Aq8QzQ4%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B0w7gB0ss2%2FLsu0tKeoNSrcBYBXxBtLn0%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1873GasXShvY75ASIc2%2FXAAsXJYJVZVq7w%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18yOFqvU3nMFPJL31BiiABVGbJgLz2Q3fg%3D; _gcl_au=1.1.564503019.1650647742; _sa=SA1.75a07a87-dc5d-46af-8c9c-ec33a83f1349.1650647742; iap.uid=7cfe3701f1144c158a57a1872455490f; adtech_uid=5ce49b07-2561-4b40-88e9-dc6b3e5df420%3Asbermarket.ru; sessionIdPostfix=react-catalog; tmr_lvid=3f5a5b054e48faf0aebcb729cfae9d41; tmr_lvidTS=1650647746371; _ym_uid=1650647747340769750; _ym_d=1650647747; __exponea_etc__=82b7ee4e-9dbd-4cdf-ba59-a8929283b0c0; _pk_id.6.3ec0=e1909fc2c9a6ab6f.1650904577.; rrpvid=97; rcuid=6292520e82847c0001a4fcda; resemble_b2b_tag=true; remember_user_token=BAhbCFsGaQP39%2B5JIhl5UmV6R05nTGUzUmpfNGphaW1LTgY6BkVGSSIXMTY1Mzc1NjYzMC4yNDEwNzMxBjsARg%3D%3D--11b06e255cf99ae28bedd4ce55d34541a61042f8; _808db7ba1248=%5B%7B%22source%22%3A%22%28direct%29%22%2C%22medium%22%3A%22%28none%29%22%2C%22cookie_changed_at%22%3A1654080270%7D%2C%7B%22source%22%3A%22sbermarket.ru%22%2C%22medium%22%3A%22referral%22%2C%22cookie_changed_at%22%3A1654080278%7D%5D; _gid=GA1.2.87396216.1653927888; tmr_detect=1%7C1654083890871; hide_pre_replacement_bubble=true; _ym_isad=1; _Instamart_session=WTl0a3pMcUV1OE5QY2FHOWFkdUFuSGZCQ2sraVdnSENLWEY0SWVGRVhKYnIyeHpjN1VzRnFqZmw3UngwQ3JjSzQveHJ5dERaR3NMVVU2SzFleVdOcTg4Smlja1VDcHZwNkQ2eHc2c0dlaWxvWllPR0U0VHlsRTZwQm11YlNzS29LcCs5L3FxeXdHOWRkVFVxV0VIL2Q5YzJCTVpzb25qRG53dEJGTGFaMVZ3cFRNSy9HMlFGbGhYVk81eHJsUTBIVStFY0Zib2xwMkhnYlVMaFJ5TG5uMzVNVktETzRLZzdoTkJpTm52d3pXbXduU1NBNGI4MUwxNEhOSUlzUkUxaEJHVTB5SHJNQTJQY1lkcDVhMFprbkgwL0UycTRWcS9ZQVgySFhrcFdLMms9LS1lcHVtOFlRNlJWMGxIeEFmdnhMUXRBPT0%3D--4214d590553490b298516c54e4d59cf493eba22b; city_info=%7B%22slug%22%3A%22perm%22%2C%22name%22%3A%22%D0%9F%D0%B5%D1%80%D0%BC%D1%8C%22%2C%22lat%22%3A58.0041%2C%22lon%22%3A56.2397%7D; _pk_ses.6.3ec0=1; pageviewCount=2; sessionId=16540838798648561069-react-catalog; top100_id=t1.7588506.1490529896.1654083881398; t2_sid_7588506=s1.1318650359.1654083881400.1654083887965.1.3.3.1; siteEntryTime=Wed%20Jun%2001%202022%2015%3A44%3A42%20GMT%2B0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); reachedTimer=0; _gat_UA-136687175-2=1; identified_address=true; identified_user=true; _ym_visorc=w; _gat_%5Bobject%20Object%5D=1; __exponea_time2__=-3607.4388065338135',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = json.dumps({"line_item":{"offer_id" : offer_id}})

    r = requests.post(
                        'https://sbermarket.ru/api/line_items', 
                        cookies=cookies, 
                        headers=headers, 
                        data=data,
                        )
    ola = r.text
    return print(ola)




if __name__ == "__main__":
    offer_id = "25484988"
    market = 'metro'
    store_id = '21'
    products = send(offer_id, market, store_id)
    print(products)
