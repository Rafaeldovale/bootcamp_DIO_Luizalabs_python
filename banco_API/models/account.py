from pydantic import BaseModel
from typing import List

class Account(BaseModel):
    id: int
    owner_name: str
    balance: float

    class Config:
        from_attributes = True

class AccountCreate(BaseModel):
    owner_name: str
    initial_deposit: float = 0.0