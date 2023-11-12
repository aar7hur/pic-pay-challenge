import pytest

from picpaychallenge.src.entities.bank_account import BankAccount
from picpaychallenge.src.entities.user import User


@pytest.fixture
def valid_bank_account(user: User) -> BankAccount:
    """Fixture for creating a valid BankAccount object.

    This fixture returns a BankAccount object with valid data for testing purposes.

    Args:
        user (User): The user associated with the bank account.

    Returns:
        BankAccount: A valid BankAccount object.
    """
    return BankAccount(account_holder="John Doe", account_number="123456789", user=user)
