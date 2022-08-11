import os
from operator import itemgetter

from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta

from .services import session
from .services import sbermarket_parser as sb_p
from .services import product_categories as p_cat
from .services import product_list as p_list
from .services import product_in_other_stores as p_other_stores
import app.services.push_product_list as ppl
from .sql_app import crud, models, schemas
from .sql_app.database import SessionLocal, engine

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="app/static", html=True), name="static")

templates = Jinja2Templates(directory="app/static/urls/")

origins = [
    "https://mindeliveryprice.ru/",
    "mindeliveryprice.ru", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)

list_markets = []
COORDS = ''

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
                "store.html",
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
                "compare.html",
                {"request": request,
                "markets_true_set": markets_true_set,
                } 
    )

@app.get("/adminpanel/admin={login}&password={password}")
async def admin_panel(login, password, request: Request):
    ''' Административная панель
    '''
    if login != "admin" or password != "admin":
        login = ""
    return templates.TemplateResponse(
        "admin_panel.html",
        {"request": request, 
        "login": login,
        }
        )    

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, crud.SECRET_KEY, algorithms=[crud.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = username
    except JWTError:
        raise credentials_exception
    user = crud.get_user(db, username=username)
    if user is None:
        raise credentials_exception
    return user


@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(db: Session = Depends(get_db), 
                                 form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=models.User)
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user

    
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
"""
if __name__ == "__main__":
    uvicorn.run("main:app", host="31.31.198.22", port=8080, reload=True)
"""