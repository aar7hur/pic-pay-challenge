from abc import ABC, abstractmethod
from typing import List

from picpaychallenge.src.entities.bank_transaction import BankTransaction
from picpaychallenge.src.interface_adapters.repositories.database_connection import IDatabaseConnection


class IBankTransactionRepository(ABC):
    """Interface representing a bank transaction repository.

    This interface defines the structure for classes that provide
    CRUD operations for bank transcations.
    """

    def __init__(self, database_connection: IDatabaseConnection) -> None:
        """Initialize the IBankAccountRepository.

        Args:
            database_connection (IDatabaseConnection): The database connection instance.
        """
        self._database_connection = database_connection

    @abstractmethod
    def create_transaction(self, transaction: BankTransaction) -> bool:
        """Create and store a new bank transaction.

        Args:
            transaction (BankTransaction): The bank transaction to be created.

        Returns:
            bool: True if the transaction creation is successful, False otherwise.
        """

    @abstractmethod
    def get_transaction_by_id(self, transaction_id: int) -> BankTransaction:
        """Retrieve a bank transaction by its unique identifier.

        Args:
            transaction_id (int): The unique identifier of the transaction.

        Returns:
            BankTransaction: The retrieved bank transaction.
        """

    @abstractmethod
    def get_all_transactions(self) -> List[BankTransaction]:
        """Retrieve a list of all bank transactions.

        Returns:
            List[BankTransaction]: The list of all bank transactions.
        """

    @abstractmethod
    def update_transaction(self, transaction: BankTransaction) -> bool:
        """Update an existing bank transaction.

        Args:
            transaction (BankTransaction): The bank transaction to be updated.

        Returns:
            bool: True if the transaction update is successful, False otherwise.
        """
