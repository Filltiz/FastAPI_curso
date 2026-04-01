# No terminal:  uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

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