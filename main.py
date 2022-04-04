import os
import json
from urllib import response

from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from dotenv import load_dotenv

import sbermarket_parser as sb_p

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
    market = markets[0]
    market = json.dumps(market)
    return  market


