from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random

from app.database.database import get_db
from app.models.user import User
from app.models.account import Account
from app.schemas.account import AccountCreate
from app.schemas.payment import SendMoney
from app.services.payment_service import send_money
from app.auth.security import verify_token

router = APIRouter()


@router.post("/account/create/{user_id}")
def create_account(
    user_id: int,
    account: AccountCreate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    existing = db.query(Account).filter(Account.user_id == user_id).first()

    if existing:
        raise HTTPException(status_code=400, detail="Account already exists")

    account_number = str(random.randint(1000000000, 9999999999))

    new_account = Account(
        account_number=account_number,
        balance=account.initial_balance,
        user_id=user_id
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return {
        "message": "Account created successfully",
        "account_number": new_account.account_number,
        "balance": new_account.balance
    }

@router.post("/transfer")
def transfer_money(
    payment: SendMoney,
    email: str = Depends(verify_token),
    db: Session = Depends(get_db)
):
    return send_money(
        payment.sender_id,
        payment.receiver_id,
        payment.amount,
        db
    )

@router.get("/account/{user_id}")
def get_account(user_id: int, db: Session = Depends(get_db)):

    account = db.query(Account).filter(
        Account.user_id == user_id
    ).first()

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return {
        "account_number": account.account_number,
        "balance": account.balance
    }