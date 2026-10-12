from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.models.wallet import Wallet

router = APIRouter()


@router.post("/wallet/create/{user_id}")
def create_wallet(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()

    if wallet:
        raise HTTPException(status_code=400, detail="Wallet already exists")

    new_wallet = Wallet(
        user_id=user_id,
        balance=0
    )

    db.add(new_wallet)
    db.commit()
    db.refresh(new_wallet)

    return {
        "message": "Wallet created successfully",
        "wallet_id": new_wallet.id,
        "balance": new_wallet.balance
    }

from app.schemas.wallet import DepositRequest

@router.post("/wallet/deposit/{user_id}")
def deposit_money(
    user_id: int,
    deposit: DepositRequest,
    db: Session = Depends(get_db)
):
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()

    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    if deposit.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")

    wallet.balance += deposit.amount

    db.commit()
    db.refresh(wallet)

    return {
        "message": "Money deposited successfully",
        "current_balance": wallet.balance
    }

@router.get("/wallet/balance/{user_id}")
def get_wallet_balance(
    user_id: int,
    db: Session = Depends(get_db)
):
    wallet = db.query(Wallet).filter(
        Wallet.user_id == user_id
    ).first()

    if not wallet:
        raise HTTPException(
            status_code=404,
            detail="Wallet not found"
        )

    return {
        "user_id": user_id,
        "balance": wallet.balance
    }