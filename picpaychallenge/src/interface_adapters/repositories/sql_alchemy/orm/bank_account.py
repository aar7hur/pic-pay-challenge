from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class BankAccountORM(Base):
    """ORM class representing a bank account in the database.

    This class defines the schema for the 'bank_accounts' table and includes
    relationships with other ORM classes.

    Attributes:
        id (str): Primary key identifier for the bank account.
        account_holder (str): The name of the account holder.
        account_number (str): The unique account number associated with the bank account.
        balance (float): The current balance of the bank account.
        created_at (datetime): The timestamp indicating when the bank account was created.
        updated_at (datetime): The timestamp indicating when the bank account was last updated.
        user_id (int): Foreign key referencing the user to whom the bank account belongs.
        user (UserORM): Relationship with the UserORM class representing the owner of the bank account.
        transactions (List[TransactionORM]): Relationship with the TransactionORM class representing the bank transactions associated with the account.
    """

    __tablename__ = "bank_accounts"

    id = Column(String, primary_key=True)
    account_holder = Column(String, nullable=False)
    account_number = Column(String, nullable=False, unique=True)
    balance = Column(Float, nullable=False, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserORM", back_populates="bank_accounts")
    transactions = relationship("TransactionORM", back_populates="account")
