from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# Cria a conexão do banco de dados
db = create_engine('sqlite:///banco.db')

# Cria a base do banco de dados
Base = declarative_base()

# Criar as classes/tabelas do Banco
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

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    status = Column("status",String)
    usuario = Column("usuario",ForeignKey("usuarios.nome"),nullable=False)
    preco = Column("preco",Float, nullable=False)
    itens = Column("itens",String, nullable=False)

# ItensPedido

# Executa a criação dos metadados do seu banco

