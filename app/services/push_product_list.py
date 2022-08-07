
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

    CONNECTION.headers.update(updated_header_field) 

    for product in legacy_product_id:
        line_item = {"line_item": {"offer_id": product}}
        json_line_item = json.dumps(line_item)

        CONNECTION.post(
                          'https://sbermarket.ru/api/line_items', 
                          data = json_line_item,
                         )

if __name__ == "__main__":
    legacy_product_id = ["12680662"]
    market = 'metro'
    store_id = '21'
    products = send(legacy_product_id, market, store_id)
    print(products)
