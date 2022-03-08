from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
FIRST_SECRET= '123'

templates = Jinja2Templates(directory="")

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, 
        "ola": FIRST_SECRET}
        )
