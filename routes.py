from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema.<br>
    Todas as rotas dos pedidos precisam de autentificação.
    """
    return {"mensagem": "Vocé acessou a rota de pedidos"}