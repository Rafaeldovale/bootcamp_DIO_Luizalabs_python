from fastapi import APIRouter, Depends, status
from models.transaction import TransactionRequest, TransactionType, Transaction
from services.transaction_service import process_transaction
from .auth import get_current_user 

router = APIRouter(
    prefix="/transactions",
    tags=["Transações"],
    dependencies=[Depends(get_current_user)] 
)

@router.post(
    "/deposit", 
    response_model=Transaction, 
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar um Depósito",
    description="Permite cadastrar um depósito na conta especificada. O valor deve ser positivo."
)
async def make_deposit(req: TransactionRequest):
    return await process_transaction(req, TransactionType.DEPOSIT)

@router.post(
    "/withdrawal", 
    response_model=Transaction, 
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar um Saque",
    description="Permite cadastrar um saque na conta especificada. Valida se o saldo é suficiente."
)
async def make_withdrawal(req: TransactionRequest):
    return await process_transaction(req, TransactionType.WITHDRAWAL)