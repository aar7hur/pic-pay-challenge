from datetime import datetime
from typing import Dict, Union

from pytest import fixture

from picpaychallenge.src.entities.bank_transaction import BankTransaction, TransactionType

BANK_TRANSACTION_DATA_TYPE = Dict[str, Union[float, datetime, TransactionType, str]]


@fixture
def valid_bank_transaction_data_dict() -> BANK_TRANSACTION_DATA_TYPE:
    """Fixture for generating valid data for BankTransaction testing.

    Returns:
        TRANSACTION_DATA_TYPE: A dictionary containing valid data for creating a BankTransaction.

    """
    # Arrange
    return {
        "type": TransactionType.DEPOSIT,
        "account_id": "123456789",
        "amount": 50.0,
        "date": datetime.now(),
    }


@fixture
def bank_transaction_entity(valid_bank_transaction_data_dict: BANK_TRANSACTION_DATA_TYPE) -> BankTransaction:
    """Fixture for creating a BankTransaction entity with valid data.

    Args:
        valid_bank_transaction_data_dict (TRANSACTION_DATA_TYPE): Valid data for creating a BankTransaction.

    Returns:
        BankTransaction: A BankTransaction entity with valid data.

    """
    return BankTransaction(**valid_bank_transaction_data_dict)
