from pydantic import BaseModel


class AccountCreate(BaseModel):
    initial_balance: float = 0