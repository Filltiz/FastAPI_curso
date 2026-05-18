from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils.types import ChoiceType

# O alembic serve para fazer uma migração do um banco de dados de uma maneira segura
# Migrar o banco de dodos
# Criar a migração: alembic revision --autogenerate -m "mensagem"
# Executar a migração: alembic upgrade head

# Cria a conexão do banco de dados
db = create_engine('sqlite:///banco.db')

# Cria a base do banco de dados
Base = declarative_base()

# Criar as classes/tabelas do Banco

# Usuários
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome",String)
    email = Column("email",String, nullable=False)
    senha = Column("senha",String)
    ativo = Column("ativo",Boolean)
    admin = Column("admin",Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


# Pedidos
class Pedido(Base):
    __tablename__ = "pedidos"

    #STATUS_PEDIDOS = (
     #   ("PENDENTE", "PENDENTE"),
     #   ("CANCELADO", "CANCELADO"),
     #   ("FINALIZADO", "FINALIZADO")
    #)

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    status = Column("status",String) # pedente, cancelado, finalizado
    usuario = Column("usuario",ForeignKey("usuarios.id"))
    preco = Column("preco",Float)
    itens = relationship("ItensPedido", cascade="all, delete")

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status

    def calcular_preco(self):
        # Percorrer todos os itens do pedido
        # Somar todos os preços todos os itens dos pedidos
        # Editar no campo "preco" o valor final do preço do pedido
        self.preco = sum(item.preco_unitario * item.quantidade for item in self.itens)


# ItensPedido
class ItensPedido(Base):
    __tablename__ = "itens_pedidos"

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade",Integer)
    sabor = Column("sabor",String)
    tamanho = Column("tamanho",String)
    preco_unitario = Column("preco_unitario",Float)
    pedido = Column("pedido",ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

# Executa a criação dos metadados do seu banco

