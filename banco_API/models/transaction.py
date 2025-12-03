from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class TransactionType(str, Enum):
    DEPOSIT = "DEPOSITO"
    WITHDRAWAL = "SAQUE"

class TransactionBase(BaseModel):
    amount: float = Field(..., gt=0, description="O valor deve ser positivo")


class TransactionRequest(TransactionBase):
    account_id: int

class Transaction(TransactionBase):
    id: int
    account_id: int
    type: TransactionType
    timestamp: datetime

    class Config:
        from_attributes = True