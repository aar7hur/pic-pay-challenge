from typing import List, Union

from picpaychallenge.src.entities.bank_transaction import BankTransaction, TransactionType
from picpaychallenge.src.entities.base_entity import BaseEntity
from picpaychallenge.src.entities.user import User


class BankAccount(BaseEntity):
    """Represents a bank account."""

    account_holder: str
    account_number: str
    user: User
    balance: float = 0.0
    transaction_history: List[BankTransaction] = []

    def deposit(self, amount: Union[float, int]) -> bool:
        """Deposit funds into the account.

        Args:
            amount (float): The amount to be deposited.

        Returns:
            bool: True if the deposit was successful, False otherwise.
        """
        if amount > 0:
            self.balance += amount
            self._record_transaction(TransactionType.DEPOSIT, float(amount))
            return True
        return False

    def withdraw(self, amount: Union[float, int]) -> bool:
        """Withdraw funds from the account.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._record_transaction(TransactionType.WITHDRAWAL, amount)
            return True
        return False

    def get_balance(self) -> float:
        """Get the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self.balance

    def get_transaction_history(self) -> List[BankTransaction]:
        """Get the transaction history of the account.

        Returns:
            List[BankTransaction]: The list of bank transactions.
        """
        return self.transaction_history

    def _record_transaction(self, transaction_type: TransactionType, amount: float):
        """Record a transaction in the history.

        Args:
            transaction_type (TransactionType): The type of transaction (e.g., "deposit", "withdrawal").
            amount (float): The amount involved in the transaction.
        """
        transaction = BankTransaction(account_id=self.id, amount=amount, type=transaction_type)
        self.transaction_history.append(transaction)
