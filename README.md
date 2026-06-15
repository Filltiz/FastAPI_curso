# 🍕 PizzaMaster - Sistema de Pedidos Completo com FastAPI

Este é um projeto completo de sistema de pedidos para pizzaria, integrando uma API robusta desenvolvida em **FastAPI** (Python) e um frontend dinâmico renderizado via **Jinja2Templates** com conexão assíncrona (JavaScript Fetch API).

O projeto implementa autenticação segura via tokens JWT (JSON Web Tokens), controle de histórico de pedidos do usuário e um painel de controle administrativo completo para gerenciamento de entregas.

---

## 🛠️ Tecnologias Utilizadas

### Backend & Banco de Dados:
* [Python 3.10+](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/) - Framework web moderno de alta performance.
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para mapeamento e manipulação de banco de dados SQL.
* [SQLite](https://www.sqlite.org/) - Banco de dados relacional leve para armazenamento local.
* [Alembic](https://alembic.sqlalchemy.org/) - Ferramenta de versionamento e migrações de banco de dados.
* [PyJWT (python-jose)](https://github.com/mpdavis/python-jose) - Geração e verificação de tokens JWT.
* [Passlib (Bcrypt)](https://passlib.readthedocs.io/) - Hash seguro e verificação de senhas dos usuários.
* [Pydantic](https://docs.pydantic.dev/) - Schemas para validação e serialização de dados de entrada/saída.

### Frontend:
* HTML5, CSS3 (variáveis customizadas, efeitos hover e micro-animações responsivas).
* JavaScript (Fetch API para requisições assíncronas, manipulação do DOM e `localStorage` para tokens JWT).

---

## 📐 Estrutura do Banco de Dados (Modelos)

O banco de dados é composto por 3 tabelas principais mapeadas via SQLAlchemy:

```
  +--------------+          +---------------+          +------------------+
  |   usuarios   |          |    pedidos    |          |  itens_pedidos   |
  +--------------+          +---------------+          +------------------+
  | id (PK)      | <------+ | id (PK)       | <------+ | id (PK)          |
  | nome         |          | status        |          | quantidade       |
  | email        |          | usuario (FK)  |          | sabor            |
  | senha        |          | preco         |          | tamanho          |
  | ativo        |          +---------------+          | preco_unitario   |
  | admin        |                                     | pedido (FK)      |
  +--------------+                                     +------------------+
```

1. **Usuario**: Guarda informações cadastrais e define privilégios do sistema (`admin` ou usuário comum).
2. **Pedido**: Controla os status (`PENDENTE`, `CANCELADO` ou `FINALIZADO`) e calcula o preço total do pedido dinamicamente a partir dos itens.
3. **ItensPedido**: Detalha cada item adicionado ao pedido (sabor, tamanho, quantidade e preço unitário).

---

## 🚀 Como Executar o Projeto Localmente

Siga o passo a passo abaixo para rodar a aplicação na sua máquina:

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Configurar o ambiente virtual (Virtual Environment)
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# No Windows (PowerShell):
.venv\Scripts\Activate.ps1
# No Linux/macOS:
source .venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente
Crie um arquivo chamado `.env` na raiz do projeto e defina as variáveis necessárias:
```env
SECRET_KEY=sua_chave_secreta_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Executar as migrações do Banco de Dados
```bash
alembic upgrade head
```

### 6. Executar o servidor de desenvolvimento
```bash
python -m uvicorn app.main:app --reload
```
O servidor estará rodando em [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 🔑 Fluxo de Conexão Frontend-Backend (JWT)

A integração e proteção de rotas no projeto seguem as seguintes etapas:
1. **Autenticação**: O usuário envia credenciais para `/auth/login` e o backend retorna um token JWT.
2. **Sessão**: O JavaScript do navegador captura o token e o salva no `localStorage`.
3. **Headers das Requisições**: Para qualquer operação protegida (Ex: finalizar pedido, listar histórico), o frontend injeta o token no cabeçalho HTTP:
   ```javascript
   headers: {
       "Authorization": "Bearer <SEU_TOKEN_AQUI>"
   }
   ```
4. **Proteção**: O backend decodifica o JWT a cada requisição e bloqueia acessos não autorizados.

---

## 👤 Desenvolvido por
Seu Nome - [Seu LinkedIn](https://www.linkedin.com/in/seu-perfil/)
