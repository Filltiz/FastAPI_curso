# No terminal:  uvicorn main:app --reload
import os

from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from auth import auth_router
from routes import order_router

app.include_router(auth_router)
app.include_router(order_router)
itens = []

@app.get("/")
def root():
    return {"Olá": "Mundo"}


@app.get("/itens")
def create_item(item: str):
    itens.append(item)
    return itens

@app.get("/itens/item_id")
def get_item(item_id: int) -> str:
    item = itens[item_id]
    return item