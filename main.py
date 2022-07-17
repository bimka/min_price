import os
from operator import itemgetter
import uvicorn

from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from requests import request

import session 
import sbermarket_parser as sb_p
import product_categories as p_cat
import product_list as p_list
import product_in_other_stores as p_other_stores
import push_product_list as ppl


load_dotenv()

app = FastAPI(debug = True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="")

origins = [
    "https://mindeliveryprice.ru/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)


class Market(BaseModel):
    id: str
    store_id: int
    name: str
    logo_image: str
    retailer: str

class Product(BaseModel):
    pass

list_markets = []
COORDS = ''

@app.get("/")
async def get(request: Request):
    ''' Главная страница
    '''
    return templates.TemplateResponse(
        "index.html",
        {"request": request, 
        "YANDEX_MAPS_API_KEY": os.getenv('YANDEX_MAPS_API_KEY'),}
        )

@app.post('/')
async def add_address(request: Request):
    ''' Функция запрашивает доступные магазины с доставкой по
        указанному адресу
    '''
    
    global COORDS
    COORDS = await request.json()
    global CONNECTION
    CONNECTION = session.establish_connection()
    markets = sb_p.get_markets(CONNECTION, COORDS)
    global list_markets  # очищаем список перед каждым вызовом
    list_markets = markets
    return list_markets
    

@app.get("/{market_name}/sid={market_id}")
async def get_store_products(request: Request, market_id):
    '''Функция отправляет список категорий продаваемых товаров для
       магазина по market_id    
    '''
    # Найдем конкретный магазин из всех объектов
    for market in list_markets:
        if market['store_id'] == int(market_id):  
            categories = p_cat.get_categories(CONNECTION, market_id)          
            return templates.TemplateResponse(
                "static/urls/store.html",
                {"request": request, 
                'categories': categories, 
                'market': market, 
                }
            )

@app.post("/send_product_list")
async def send_product_list(request: Request):
    '''Функция отправляет список продуктов для данной 
       категории товаров
    '''
    url , store_id = await request.json()
    product_list = p_list.get_products(CONNECTION, url, store_id)
    return product_list

@app.get("/compare/order={order}")
async def compare_order(order, request: Request):
    '''Функция сравнивает заказ пользователя в разных магазинах
    '''
    order_list = order.split('&')
    # добавляем в markets_true_set магазины в которых весь набор 
    # продуктов имеется в наличии
    markets_true_set = []
    for market in list_markets: # проверяем все магазины
        confirmed_prod = [market] # сразу добавляем инфу о магазине
        total_price = 0 
        for product in order_list: # проверяем наличие всех продуктов
            # добавляем в confirmed_prod продукты, которые есть в 
            # магазине. Потом если количество в order_list и 
            # confirmed_prod совпадут, то добавляем магазин 
            # в markets_true_set
            try:
                info =   p_other_stores.get(CONNECTION, market['retailer']['slug'], market['store_id'], product)
                print('info: ', info)
                if info['product']['offer']['price']:
                    confirmed_prod.append(info)
                    total_price += float(info['product']['offer']['price'])
                    total_price = round(float(total_price), 2)

            except:
                break
        confirmed_prod.append(total_price)
        if len(order_list) + 2 == len(confirmed_prod): # на 2 больше т.к.
            # дополнительно идет информация о магазине и общая цена
            markets_true_set.append(confirmed_prod)
    # сортируем список по возрастанию общей цены
    markets_true_set = sorted(markets_true_set, key=itemgetter(-1))
        
    return templates.TemplateResponse(
                "static/urls/compare.html",
                {"request": request,
                "markets_true_set": markets_true_set,
                } 
    )
    
"""
@app.post("/push_product_list")
async def push_product_list(request: Request):
    '''Функция отправляет список продуктов в Сбермаркет 
       для их отображения в корзине
       Перед этим отправляем координты для получения адреса

       ФУНКЦИЯ НА ДАННЫЙ МОМЕНТ НЕ РЕАЛИЗУЕМА!!!
       ЗАДЕЛ НА БУДЕЩЕЕ
       КУКИ БЕРУТСЯ ИЗ НЕОТКУДА, ПОКА НЕТ ВОЗМОЖНОСТИ ПЕРЕХВАТИТЬ
    '''
    legacy_product_id , market, store_id = await request.json()
    ppl.send(CONNECTION, legacy_product_id, market, store_id)
"""

if __name__ == '__main__':
    uvicorn.run('main:app', port=80, host='31.31.198.22')