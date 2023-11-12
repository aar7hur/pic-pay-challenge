from abc import ABC, abstractmethod
from typing import List, Optional

from picpaychallenge.src.entities.bank_account import BankAccount
from picpaychallenge.src.interface_adapters.repositories.database_connection import IDatabaseConnection


class IBankAccountRepository(ABC):
    """Interface representing a bank account repository.

    This interface defines the structure for classes that provide
    CRUD operations for bank accounts.
    """

    def __init__(self, database_connection: IDatabaseConnection) -> None:
        """Initialize the IBankAccountRepository.

        Args:
            database_connection (IDatabaseConnection): The database connection instance.
        """
        self._database_connection = database_connection

    @abstractmethod
    def get_by_account_number(self, account_number: str) -> Optional[BankAccount]:
        """Retrieve a bank account by its account number.

        Args:
            account_number (str): The account number of the bank account.

        Returns:
            BankAccount: The retrieved bank account.
        """

    @abstractmethod
    def get_all_accounts(self) -> List[Optional[BankAccount]]:
        """Retrieve a list of all bank accounts.

        Returns:
            List[BankAccount]: The list of all bank accounts.
        """

    @abstractmethod
    def create_account(self, bank_account: BankAccount) -> bool:
        """Create and store a new bank account.

        Args:
            bank_account (BankAccount): The bank account to be created.

        Returns:
            bool: True if the account creation is successful, False otherwise.
        """

    @abstractmethod
    def update_account(self, bank_account: BankAccount) -> bool:
        """Update an existing bank account.

        Args:
            bank_account (BankAccount): The bank account to be updated.

        Returns:
            bool: True if the account update is successful, False otherwise.
        """
