from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime

from app.database.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    sender_id = Column(Integer, ForeignKey("users.id"))

    receiver_id = Column(Integer, ForeignKey("users.id"))

    amount = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)