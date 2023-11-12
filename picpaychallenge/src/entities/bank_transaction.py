from __future__ import annotations

from datetime import datetime
from enum import Enum, auto
from typing import Union

from pydantic import PositiveFloat, field_validator

from picpaychallenge.src.entities.base_entity import BaseEntity


class TransactionType(Enum):
    """Enumeration representing types of bank transactions."""

    WITHDRAWAL = auto()
    DEPOSIT = auto()


class BankTransaction(BaseEntity):
    """Model representing a bank transaction."""

    type: Union[TransactionType, str]
    account_id: str
    amount: PositiveFloat
    date: datetime = datetime.now()

    @field_validator("type")
    @classmethod
    def type_belongs_to_transaction_type(cls, value: Union[str, TransactionType]) -> TransactionType:
        """Validate and convert the transaction type to TransactionType enum.

        Args:
            value (Union[str, TransactionType]): The transaction type input.

        Returns:
            TransactionType: The converted TransactionType enum.

        Raises:
            ValueError: If the transaction type is invalid.

        """
        try:
            return TransactionType(value) if isinstance(value, str) else value
        except ValueError:
            raise ValueError("Invalid transaction type")
