
def get_products(CONNECTION, url, store_id):
    '''Функция отправляет GET-запрос, возвращая список товаров
    ''' 
    split_url = url.split('/')
    inserts = []
    
    for i in split_url[::-1]:
        if i != 'categories':
             inserts.append(i)
        else:
            inserts.append(store_id)
            break
    inserts = inserts[::-1]         
    moditify_url = make_path(inserts)

    response = CONNECTION.get(
            moditify_url, 
            )
    data = response.json()
    
    return data['products']    

def make_path(*args):
    '''Функция собирает url
    '''
    store_id = args[0][0]
    path_vars = '/'.join(args[0][1:])
    return f"https://sbermarket.ru/api/stores/{ store_id }/products?tid={ path_vars }&page=1&per_page=100&sort=popularity"

if __name__ == "__main__":
    url = 'https://sbermarket.ru/api/stores/10/products?tid=moloko-iaitsa-new/moloko&page=1&per_page=24&sort=popularity'
    store_id = str(1373)
    products = get_products(url, store_id)
    print(products)
