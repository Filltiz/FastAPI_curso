# No terminal:  uvicorn app.main:app --reload
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login-form")


# Essas importações estão aqui para não ocorre erros
from app.internal.auth import auth_router
from app.routers.routes import order_router

app.include_router(auth_router)
app.include_router(order_router)
itens = []

# Configura o diretório onde estão os arquivos HTML
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@app.get("/pedidos", response_class=HTMLResponse)
def pedidos_page(request: Request):
    return templates.TemplateResponse(request=request, name="pedidos.html")


@app.get("/admin", response_class=HTMLResponse)
def admin_page(request: Request):
    return templates.TemplateResponse(request=request, name="admin.html")


@app.get("/itens")
def create_item(item: str):
    itens.append(item)
    return itens

@app.get("/itens/item_id")
def get_item(item_id: int) -> str:
    item = itens[item_id]
    return item