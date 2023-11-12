# picpaychallenge/src/interfaces/database_connection.py

from abc import ABC, abstractmethod


class IDatabaseConnection(ABC):
    def __init__(self, database_url: str) -> None:
        self._database_url = database_url

    @abstractmethod
    def connect(self):
        """Method to establish a connection to the database."""
