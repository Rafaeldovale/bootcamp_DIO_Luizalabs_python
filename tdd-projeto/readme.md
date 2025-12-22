🏋️‍♂️ Workout API - DIO
Esta é uma API assíncrona para gerenciamento de atletas de uma academia, desenvolvida como projeto prático para a DIO (Digital Innovation One). O projeto utiliza o framework FastAPI, o banco de dados MongoDB e segue os princípios de TDD (Test Driven Development).

🛠️ Tecnologias Utilizadas
Python 3.11+

FastAPI: Framework web de alta performance.

Pydantic: Validação de dados e Schemas.

Motor: Driver assíncrono para MongoDB.

Pytest: Ferramenta para testes automatizados.

Uvicorn: Servidor ASGI para rodar a aplicação.

📁 Estrutura do Projeto
Plaintext

workout_api/
├── workout_api/
│   ├── atleta/           # Schemas e Controllers dos atletas
│   ├── db/               # Configuração da conexão com MongoDB
│   └── main.py           # Ponto de entrada da aplicação
├── tests/                # Testes unitários e de integração
├── requirements.txt      # Dependências do projeto
└── README.md
🚀 Como Executar o Projeto
1. Clonar o repositório e configurar o ambiente
Bash

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
.\venv\Scripts\activate

# Ativar ambiente (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
2. Configurar o Banco de Dados
Certifique-se de que o MongoDB está rodando (via Docker ou localmente) na porta 27017.

3. Rodar a API
Bash

uvicorn workout_api.main:app --reload
📖 Documentação (Swagger)
Com a API rodando, acesse a documentação interativa para testar os endpoints: 🔗 http://127.0.0.1:8000/docs

🧪 Rodando os Testes (TDD)
Para garantir que tudo está funcionando conforme o esperado, execute:

Bash

pytest