# picpaychallenge/src/infrastructure/sqlalchemy_database_connection.py

from sqlalchemy import create_engine

from picpaychallenge.src.interface_adapters.repositories.database_connection import IDatabaseConnection


class SQLAlchemyDatabaseConnection(IDatabaseConnection):
    def __init__(self, database_url: str) -> None:
        super().__init__(database_url)

    def connect(self):
        self.engine = create_engine(self._database_url)
