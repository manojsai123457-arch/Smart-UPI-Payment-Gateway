from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.wallet import Wallet


def send_money(sender_id: int, receiver_id: int, amount: float, db: Session):

    if amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Amount must be greater than zero"
        )

    sender = db.query(Wallet).filter(
        Wallet.user_id == sender_id
    ).first()

    receiver = db.query(Wallet).filter(
        Wallet.user_id == receiver_id
    ).first()

    if not sender:
        raise HTTPException(
            status_code=404,
            detail="Sender wallet not found"
        )

    if not receiver:
        raise HTTPException(
            status_code=404,
            detail="Receiver wallet not found"
        )

    if sender.balance < amount:
        raise HTTPException(
            status_code=400,
            detail="Insufficient balance"
        )

    sender.balance -= amount
    receiver.balance += amount

    db.commit()

    return {
        "message": "Money transferred successfully",
        "sender_balance": sender.balance,
        "receiver_balance": receiver.balance
    }