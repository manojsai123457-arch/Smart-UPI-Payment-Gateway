from fastapi import FastAPI

from app.database.database import engine
from app.database.base import Base

# Import models
from app.models.user import User
from app.models.wallet import Wallet
from app.models.account import Account   # <-- Add this

# Import routers
from app.api.user import router as user_router
from app.api.account import router as account_router
from app.api.wallet import router as wallet_router
from app.models.transaction import Transaction
from app.api.transaction import router as transaction_router
from app.api.history import router as history_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart UPI Payment Gateway API",
    description="Backend API for a UPI-inspired payment system",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(account_router)   
app.include_router(wallet_router)
app.include_router(transaction_router)
app.include_router(history_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Smart UPI Payment Gateway API"
    }