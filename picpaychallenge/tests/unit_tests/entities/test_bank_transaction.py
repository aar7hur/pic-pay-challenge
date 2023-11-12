from datetime import datetime

import pytest
from pydantic import ValidationError

from picpaychallenge.src.entities.bank_transaction import BankTransaction, TransactionType
from picpaychallenge.tests.fixtures.bank_transaction import BANK_TRANSACTION_DATA_TYPE


def test_bank_transaction_model_valid(valid_bank_transaction_data_dict: BANK_TRANSACTION_DATA_TYPE):
    """Test BankTransaction model with valid data.

    Args:
        valid_bank_transaction_data_dict (BANK_TRANSACTION_DATA_TYPE): Valid data for creating a BankTransaction.
    """
    # Act
    transaction = BankTransaction(**valid_bank_transaction_data_dict)

    # Assert
    assert transaction.type == valid_bank_transaction_data_dict["type"]
    assert transaction.account_id == valid_bank_transaction_data_dict["account_id"]
    assert transaction.amount == valid_bank_transaction_data_dict["amount"]
    assert transaction.date == valid_bank_transaction_data_dict["date"]


def test_bank_transaction_model_invalid_amount():
    """Test BankTransaction model with invalid amount."""
    # Arrange
    invalid_data = {
        "type": TransactionType.WITHDRAWAL,
        "account_id": "987654321",
        "amount": -10.0,  # Invalid, amount must be positive
        "date": datetime.now(),
    }

    # Act & Assert
    with pytest.raises(ValidationError):
        BankTransaction(**invalid_data)


def test_bank_transaction_model_invalid_type():
    """Test BankTransaction model with invalid transaction type."""
    # Arrange
    invalid_data = {
        "type": "INVALID_TYPE",  # Invalid transaction type
        "account_id": "987654321",
        "amount": 20.0,
        "date": datetime.now(),
    }

    # Act & Assert
    with pytest.raises(ValueError, match="Invalid transaction type"):
        BankTransaction(**invalid_data)
