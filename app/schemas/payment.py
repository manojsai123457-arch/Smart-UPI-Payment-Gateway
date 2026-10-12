from pydantic import BaseModel


class SendMoney(BaseModel):
    sender_id: int
    receiver_id: int
    amount: float