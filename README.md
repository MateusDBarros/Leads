# 🤖 API Chatbot para Captura de Leads

## ✨ Descrição

Este projeto é uma API de Chatbot desenvolvida com Flask, integrada a um banco de dados PostgreSQL, e um frontend em HTML, CSS e JavaScript. O chatbot coleta informações de potenciais clientes (leads) e armazena no banco para posterior análise e contato.

##  Tecnologias Utilizadas

### Backend: Flask (Python)

### Banco de Dados: PostgreSQL

### Frontend: HTML, CSS, JavaScript

### ORM: SQLAlchemy (para manipulação do banco de dados)


## 🔧 Instalação e Configuração

Antes de rodar o projeto, siga os passos abaixo para configurar o ambiente:

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/MateusDBarros/chatbot-leads.git
cd chatbot-leads
```

## 2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

## 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

## 4️⃣ Configurar o banco de dados PostgreSQL

Crie um banco de dados no PostgreSQL e configure as credenciais no arquivo .env:
```bash
DATABASE_URL=postgresql://usuario:senha@localhost:5432/chatbot_db
```
## 5️⃣ Executar as migrações do banco
```bash
flask db init
flask db migrate -m "Inicializando o banco"
flask db upgrade
```

## 🚀 Como Rodar o Projeto

### 🔹 Rodando o Backend (API Flask)
```bash
flask run
```
A API estará disponível em: http://127.0.0.1:5000/

### 🔹 Rodando o Frontend

Abra o arquivo index.html no navegador ou utilize um servidor local:
```bash
python -m http.server 8080  # Para rodar localmente
```
O frontend estará disponível em: http://127.0.0.1:8080/
