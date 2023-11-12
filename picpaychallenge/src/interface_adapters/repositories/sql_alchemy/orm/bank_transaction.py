from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class TransactionORM(Base):
    """ORM class representing a bank transaction in the database.

    This class defines the schema for the 'transactions' table and includes
    relationships with other ORM classes.

    Attributes:
        id (str): Primary key identifier for the transaction.
        type (str): The type of the transaction.
        amount (float): The amount of money involved in the transaction.
        date (datetime): The timestamp indicating when the transaction occurred.
        account_id (int): Foreign key referencing the bank account associated with the transaction.
        account (BankAccountORM): Relationship with the BankAccountORM class representing the bank account involved in the transaction.
    """

    __tablename__ = "transactions"

    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    account_id = Column(Integer, ForeignKey("bank_accounts.id"))
    account = relationship("BankAccountORM", back_populates="transactions")
