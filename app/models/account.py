from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)

    account_number = Column(String(20), unique=True, nullable=False)

    balance = Column(Float, default=0)

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User")