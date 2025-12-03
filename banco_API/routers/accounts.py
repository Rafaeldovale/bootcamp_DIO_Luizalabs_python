from fastapi import APIRouter, Depends, HTTPException
from models.account import Account
from models.transaction import Transaction
from database import get_account, get_transactions_by_account
from typing import List
from .auth import get_current_user 

router = APIRouter(
    prefix="/accounts",
    tags=["Contas e Extrato"],
    dependencies=[Depends(get_current_user)] 
)

@router.get(
    "/{account_id}/statement", 
    response_model=List[Transaction],
    summary="Exibir Extrato da Conta",
    description="Retorna todas as transações realizadas para a conta especificada."
)
async def get_statement(account_id: int):
    account = await get_account(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada.")
    

    transactions = await get_transactions_by_account(account_id)
    return transactions