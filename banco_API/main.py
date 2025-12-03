from fastapi import FastAPI
from routers import auth, accounts, transactions

app = FastAPI(
    title="Bank Async RESTful API",
    description="API para gerenciamento de contas e transações bancárias (Depósito/Saque), com autenticação JWT.",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(transactions.router)

@app.get("/", tags=["Saúde"])
def read_root():
    return {"message": "API de Operações Bancárias está ONLINE."}
