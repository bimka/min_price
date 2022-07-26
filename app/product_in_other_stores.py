
def get(CONNECTION, market, store_id, product):
    """ Функция отправляет запросы с корзиной продуктов в различные 
        магазины для установления наличия и получения цены корзины
    """ 

    response = CONNECTION.get(f'https://sbermarket.ru/api/stores/{ store_id }/products/{ product }', 
        headers = {
            'Referer': f'https://sbermarket.ru/{ market }?sid={ store_id }',
            'csrf_param': None,
            'csrf_token': None, 
            'api-version': None, 
            'client-token': None, 
            'is-storefront-ssr': None,
        },
        )
        
    return response.json()

if __name__ == "__main__":
    store = 21
    product = 'moloko-3-2-ul-trapasterizovannoe-925-ml-domik-v-derevne-bzmzh-f14c772'
    
    list_markets = ['21', '15434', '420', '1373']
    order_list = ['moloko-3-2-ul-trapasterizovannoe-925-ml-domik-v-derevne-bzmzh-f14c772', 
                  'gazirovannyy-napitok-pepsi-cola-2-l-a1ba9fc',
                  ]
    markets_true_set = [] 
    for market in list_markets:
        confirmed_prod = [market]
        for product in order_list:
            try:
                info = get(market, product)
                if info['product']['offer']['price'] and \
                    info['product']['offer']['active']:
                    
                    confirmed_prod.append(info)
            except:
                break
        if len(order_list) + 1 == len(confirmed_prod):
            markets_true_set.append(confirmed_prod)

    print(len(markets_true_set))


