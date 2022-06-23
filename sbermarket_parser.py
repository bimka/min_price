import requests

def get_markets(CONNECTION, COORDS):
    ''' Функция отправляет на сервер Сбермаркета координаты доставки,
        возвращается список магазинов, совершающих доставку на данный адрес
    '''
    lat = COORDS[0]
    lon = COORDS[1]

    additional_header_fields={
        'api-version': '3.0',
        'client-token': '7ba97b6f4049436dab90c789f946ee2f', 
        'Host': 'sbermarket.ru',
        'is-storefront-ssr': 'false', 
    }
    CONNECTION.headers.update(additional_header_fields)

    response = requests.get(
        f'https://sbermarket.ru/api/stores?lat={ lat }&lon={ lon }&include=closest_shipping_options,labels,retailer&shipping_method=delivery', 
        headers = CONNECTION.headers,
        )

    return response.json()

if __name__ == "__main__":
    lat = 55.75503467371233
    lon = 37.64715556103516
    sb_markets = get_markets(lat, lon)
    print(sb_markets)
