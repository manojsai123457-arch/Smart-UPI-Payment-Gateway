from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.transaction import Transaction

router = APIRouter()


@router.get("/transactions/{user_id}")
def transaction_history(user_id: int, db: Session = Depends(get_db)):

    transactions = db.query(Transaction).filter(
        (Transaction.sender_id == user_id) |
        (Transaction.receiver_id == user_id)
    ).all()

    history = []

    for t in transactions:
        history.append({
            "transaction_id": t.id,
            "sender_id": t.sender_id,
            "receiver_id": t.receiver_id,
            "amount": t.amount,
            "created_at": t.created_at
        })

    return history