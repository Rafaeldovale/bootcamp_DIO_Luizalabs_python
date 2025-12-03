from models.account import Account
from models.transaction import Transaction

ACCOUNTS = {
    1001: Account(id=1001, owner_name="Alice Silva", balance=500.0),
    1002: Account(id=1002, owner_name="Bob Souza", balance=150.0),
}
TRANSACTIONS = [] 
NEXT_TRANSACTION_ID = 1

async def get_account(account_id: int):
    return ACCOUNTS.get(account_id)

async def get_transactions_by_account(account_id: int):
    return [t for t in TRANSACTIONS if t.account_id == account_id]