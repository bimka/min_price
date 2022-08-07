
def get_categories(CONNECTION, store_id):
    '''Функция отправляет GET-запрос, получая категории продаваемых 
       товаов в виде списка
    '''
    
    response = CONNECTION.get(
        f'https://sbermarket.ru/api/stores/{ store_id }/categories?depth=2&include='
        )

    data = response.json()
    return data['categories']

if __name__ == "__main__":
    store_id = 21
    sb_markets = get_categories(store_id)
    print(sb_markets[0])