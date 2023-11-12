from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class UserORM(Base):
    """ORM class representing a user in the database.

    This class defines the schema for the 'users' table and includes
    relationships with other ORM classes.

    Attributes:
        id (str): Primary key identifier for the user.
        username (str): The username of the user.
        cpf (str): The CPF (Brazilian tax identification number) of the user.
        email (str): The email address of the user.
        password (str): The password associated with the user.
        created_at (datetime): The timestamp indicating when the user was created.
        updated_at (datetime): The timestamp indicating when the user was last updated.
        bank_accounts (List[BankAccountORM]): Relationship with the BankAccountORM class representing the bank accounts associated with the user.
    """

    __tablename__ = "users"

    id = Column(String, primary_key=True)
    username = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)  # Add the password attribute
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    # Establish a one-to-many relationship between UserORM and BankAccountORM
    bank_accounts = relationship("BankAccountORM", back_populates="user")
