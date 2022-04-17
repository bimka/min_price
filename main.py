import os
import json
from urllib import response

from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from requests import request

import sbermarket_parser as sb_p
import product_categories as p_cat

load_dotenv()

app = FastAPI(debug = True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Market(BaseModel):
    id: str
    store_id: int
    name: str
    logo_image: str
    retailer: str

class Stores(BaseModel):
    markets: List[Market]

list_markets = []

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, 
        "YANDEX_MAPS_API_KEY": os.getenv('YANDEX_MAPS_API_KEY'),}
        )

@app.post('/')
async def add_address(request: Request):
    coords = await request.json()
    markets = sb_p.get_markets(lat = coords[0], lon = coords[1])
    for market in markets:
        raw_market = {
            'id' : market['id'],
            'store_id': market['store_id'],
            'name': market['name'],
            'logo_image': market['retailer']['appearance']['logo_image'],
            'retailer': market['retailer']['slug'],
        }
        structured_market = Market(**raw_market)
        list_markets.append(structured_market)
    return list_markets
    

@app.get("/{market_name}/sid={market_id}", response_model=Market)
async def get_store_products(request: Request, market_id, market_name):
    '''Функция отправляет список категорий продаваемых товаров для
       магазина по market_id    
    '''
    # Найдем конкретный магазин из всех объектов
    for market in list_markets:
        if market.store_id == int(market_id):  
            categories = p_cat.get_categories(market_id)          
            return templates.TemplateResponse(
                "static/urls/store.html",
                {"request": request, 
                'categories': categories, 
                'market': market, 
                }
            )

@app.post('/')
async def send_product_list(request: Request):
    '''Функция отправляет список продуктов для данной 
       категории товаров
    '''
    pass
