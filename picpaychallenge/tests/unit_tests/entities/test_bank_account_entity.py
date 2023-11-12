from __future__ import with_statement

from picpaychallenge.src.entities.bank_account import BankAccount
from picpaychallenge.src.entities.bank_transaction import BankTransaction, TransactionType


def test_deposit(valid_bank_account: BankAccount):
    """Test the deposit method of BankAccount.

    The test checks if the deposit operation increases the account balance correctly.

    Args:
        valid_bank_account (BankAccount): A valid BankAccount object.

    """
    # Arrange
    initial_balance = valid_bank_account.get_balance()

    # Act
    success = valid_bank_account.deposit(100.0)

    # Assert
    assert success
    assert valid_bank_account.get_balance() == initial_balance + 100.0


def test_withdraw(valid_bank_account: BankAccount):
    """Test the withdraw method of BankAccount.

    The test checks if the withdraw operation decreases the account balance correctly.

    Args:
        valid_bank_account (BankAccount): A valid BankAccount object.

    """
    # Arrange
    valid_bank_account.deposit(200.0)
    initial_balance = valid_bank_account.get_balance()

    # Act
    success = valid_bank_account.withdraw(50.0)

    # Assert
    assert success
    assert valid_bank_account.get_balance() == initial_balance - 50.0


def test_invalid_withdraw(valid_bank_account: BankAccount):
    """Test the withdraw method with insufficient funds.

    The test checks if the withdraw operation fails when the account balance is insufficient.

    Args:
        valid_bank_account (BankAccount): A valid BankAccount object.

    """
    # Arrange
    initial_balance = valid_bank_account.get_balance()

    # Act
    success = valid_bank_account.withdraw(50.0)

    # Assert
    assert not success
    assert valid_bank_account.get_balance() == initial_balance


def test_get_transaction_history_one_deposit(valid_bank_account: BankAccount):
    """Test the get_transaction_history method with one deposit transaction.

    Args:
        valid_bank_account (BankAccount): A valid BankAccount object.

    """
    # Arrange
    initial_balance = valid_bank_account.get_balance()
    deposit_value = 100.0
    valid_bank_account.deposit(deposit_value)

    # Act
    transaction_history = valid_bank_account.get_transaction_history()

    # Assert
    assert len(transaction_history) == 1
    transaction = transaction_history[0]
    assert transaction.amount == deposit_value
    assert transaction.type == TransactionType.DEPOSIT
    assert transaction.account_id == valid_bank_account.id
    assert valid_bank_account.get_balance() == initial_balance + deposit_value


def test_get_transaction_history_missing_balance_to_withdrawal(valid_bank_account: BankAccount):
    """Test the get_transaction_history method with one withdrawal transaction.

    Args:
        valid_bank_account (BankAccount): A valid BankAccount object.

    """
    # Arrange
    initial_balance = valid_bank_account.get_balance()
    withdraw_value = 30.0
    valid_bank_account.withdraw(withdraw_value)

    # Act
    transaction_history = valid_bank_account.get_transaction_history()

    # Assert
    assert len(transaction_history) == 0
    assert valid_bank_account.get_balance() == initial_balance


def test_get_transaction_history_more_than_one_transaction(valid_bank_account: BankAccount):
    """Test the get_transaction_history method with more than one transaction.

    The test checks if the transaction history is retrieved correctly.

    Args:
        valid_bank_account (BankAccount): A valid BankAccount object.

    """
    # Arrange
    deposit_value = 100.0
    withdraw_value = 50.0
    valid_bank_account.deposit(deposit_value)
    valid_bank_account.withdraw(withdraw_value)

    # Act
    transaction_history = valid_bank_account.get_transaction_history()

    # Assert
    assert len(transaction_history) == 2
    for transaction in transaction_history:
        assert isinstance(transaction, BankTransaction)
        assert transaction.amount in [deposit_value, withdraw_value]
        if transaction.type == TransactionType.WITHDRAWAL:
            assert transaction.amount == withdraw_value
