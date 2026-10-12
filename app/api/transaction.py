from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.wallet import Wallet
from app.models.transaction import Transaction
from app.schemas.transaction import TransferRequest

router = APIRouter()


@router.post("/transfer")
def transfer_money(
    transfer: TransferRequest,
    db: Session = Depends(get_db)
):

    sender = db.query(Wallet).filter(
        Wallet.user_id == transfer.sender_id
    ).first()

    receiver = db.query(Wallet).filter(
        Wallet.user_id == transfer.receiver_id
    ).first()

    if not sender:
        raise HTTPException(status_code=404, detail="Sender wallet not found")

    if not receiver:
        raise HTTPException(status_code=404, detail="Receiver wallet not found")

    if transfer.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    if sender.balance < transfer.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    sender.balance -= transfer.amount
    receiver.balance += transfer.amount

    transaction = Transaction(
        sender_id=transfer.sender_id,
        receiver_id=transfer.receiver_id,
        amount=transfer.amount
    )

    db.add(transaction)
    db.commit()

    return {
        "message": "Transfer Successful",
        "amount": transfer.amount
    }