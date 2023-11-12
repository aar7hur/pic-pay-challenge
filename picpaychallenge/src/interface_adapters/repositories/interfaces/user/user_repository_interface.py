from abc import ABC, abstractmethod
from typing import List, Optional

from picpaychallenge.src.entities.user import User
from picpaychallenge.src.interface_adapters.repositories.database_connection import IDatabaseConnection


class IUserRepository(ABC):
    def __init__(self, database_connection: IDatabaseConnection) -> None:
        self._database_connection = database_connection

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Retrieve a user by their email address.

        Args:
            email (str): The email address of the user.

        Returns:
            Optional[User]: The retrieved user or None if not found.
        """

    @abstractmethod
    def get_user_by_cpf(self, cpf: str) -> Optional[User]:
        """Retrieve a user by their CPF (Brazilian Social Security number).

        Args:
            cpf (str): The CPF of the user.

        Returns:
            Optional[User]: The retrieved user or None if not found.
        """

    @abstractmethod
    def get_all_users(self) -> List[User]:
        """Retrieve a list of all users.

        Returns:
            List[User]: The list of all users.
        """

    @abstractmethod
    def create_user(self, user: User) -> bool:
        """Create and store a new user.

        Args:
            user (User): The user to be created.

        Returns:
            bool: True if the user creation is successful, False otherwise.
        """

    @abstractmethod
    def update_user(self, user: User) -> bool:
        """Update an existing user.

        Args:
            user (User): The user to be updated.

        Returns:
            bool: True if the user update is successful, False otherwise.
        """
