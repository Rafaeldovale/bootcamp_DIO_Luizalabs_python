# 🏦 Bank Async RESTful API

API RESTful assíncrona desenvolvida com **FastAPI** para gerenciar operações bancárias de depósito e saque em contas correntes, com foco em alta performance e segurança (JWT).

## 🎯 Objetivos do Projeto

O objetivo principal deste projeto é demonstrar a implementação de uma API robusta com as seguintes funcionalidades:

1.  **Cadastro de Transações:** Registrar depósitos e saques em contas.
2.  **Exibição de Extrato:** Obter o histórico de transações de uma conta.
3.  **Autenticação Segura:** Utilizar **JWT (JSON Web Token)** para proteger os *endpoints*.
4.  **Validações:** Garantir a integridade das operações (ex: valor positivo, saldo suficiente para saque).

---

## 💻 Requisitos Técnicos

Antes de começar, certifique-se de ter o **Python 3.8+** instalado em seu sistema.

### 🛠️ Instalação e Configuração

#### 1. Clonar o Repositório (Se aplicável)

```bash
# git clone <URL do seu repositório>
# cd bank-api
2. Criação de Ambiente Virtual (Recomendado)
É uma boa prática isolar as dependências do projeto:
```

```Bash

python -m venv venv
# Ativar no Windows
.\venv\Scripts\activate
# Ativar no macOS/Linux
source venv/bin/activate

```


3. Instalação das Dependências
Instale todos os pacotes necessários. Note que usamos extras para garantir a criptografia e o hashing de senhas.

```Bash

pip install fastapi uvicorn "python-jose[cryptography]" "passlib[bcrypt]" python-multipart

```
fastapi: O framework principal.
uvicorn: O servidor ASGI de alta performance.
python-jose[cryptography]: Para manipular os JWTs.
passlib[bcrypt]: Para o hashing seguro de senhas.

🚀 Como Rodar a Aplicação
A API utiliza o Uvicorn. Para iniciar o servidor no modo de desenvolvimento com reload automático:

```Bash

uvicorn main:app --reload
A API estará acessível em: http://127.0.0.1:8000
```

📄 Documentação e Endpoints
O FastAPI gera automaticamente a documentação interativa da API, que está de acordo com o padrão OpenAPI/Swagger UI.

1. Acesso à Documentação
Após iniciar o servidor, acesse:

Ferramenta	Link
Swagger UI (Interativa)	http://127.0.0.1:8000/docs
ReDoc (Visualização Limpa)	http://127.0.0.1:8000/redoc

Exportar para as Planilhas

2. Fluxo de Uso e Endpoints Protegidos
Todos os endpoints de transação e extrato exigem um Token de Acesso JWT.

🔑 Autenticação (Etapa Obrigatória)
Método	Caminho	Descrição
POST	/auth/token	Login. Recebe username e password (via form data) e retorna um access_token JWT.

Exportar para as Planilhas

Exemplo de Credenciais (Simuladas):

Username: admin

Password: secret

💰 Transações (Requer Token)
Método	Caminho	Descrição
POST	/transactions/deposit	Cadastra um Depósito. Requer account_id e amount.
POST	/transactions/withdrawal	Cadastra um Saque. Requer account_id e amount. Valida o saldo da conta.

Exportar para as Planilhas

📈 Contas e Extrato (Requer Token)
Método	Caminho	Descrição
GET	/accounts/{account_id}/statement	Exibe o Extrato. Retorna a lista completa de transações para a conta fornecida.

Exportar para as Planilhas

📐 Estrutura do Projeto
O projeto segue uma arquitetura modular para separar responsabilidades:

Diretório/Arquivo	Responsabilidade
main.py	Instância principal do FastAPI e roteamento.
database.py	Simulação de persistência de dados (Contas/Transações).
models/	Modelos Pydantic para tipagem e validação de dados.
routers/	Agrupamento de endpoints por funcionalidade (auth, accounts, transactions).
services/	Lógica de Negócio. Implementação de validações (saldo) e manipulação de JWT.