from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import PedidoSchema
from models import Pedido

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema.<br>
    Todas as rotas dos pedidos precisam de autentificação.
    """
    return {"mensagem": "Vocé acessou a rota de pedidos"}

@order_router.post("/pedidos")
async def criar_pedidos(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}
