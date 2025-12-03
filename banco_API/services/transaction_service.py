from fastapi import HTTPException
from models.transaction import TransactionRequest, TransactionType, Transaction
from database import ACCOUNTS, NEXT_TRANSACTION_ID, TRANSACTIONS 
from datetime import datetime

async def process_transaction(req: TransactionRequest, type: TransactionType) -> Transaction:
    global NEXT_TRANSACTION_ID

    account = ACCOUNTS.get(req.account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if req.amount <= 0:
        raise HTTPException(status_code=400, detail="O valor da transação deve ser positivo.")
    
    new_balance = account.balance
    
    if type == TransactionType.DEPOSIT:
        new_balance += req.amount
    
    elif type == TransactionType.WITHDRAWAL:
        if account.balance < req.amount:
            raise HTTPException(status_code=400, detail="Saldo insuficiente para saque.")
        new_balance -= req.amount
    

    account.balance = new_balance
    
    new_transaction = Transaction(
        id=NEXT_TRANSACTION_ID,
        account_id=req.account_id,
        amount=req.amount,
        type=type,
        timestamp=datetime.now()
    )
    
    TRANSACTIONS.append(new_transaction)
    NEXT_TRANSACTION_ID += 1
    
    return new_transaction