import os

from dotenv import load_dotenv


class SingletonMeta(type):
    """Singleton metaclass.

    This metaclass ensures that only one instance of a class is created.

    Attributes:
        _instances (dict): A dictionary to store instances of classes.

    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Create or return the instance of the class.

        Args:
            cls: The class to instantiate.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            cls: The instance of the class.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    """Singleton configuration class.

    This class reads configuration from environment variables using dotenv
    and ensures that only one instance of the configuration is created.
    """

    def __init__(self, config_path: str = ".env"):
        """Initialize the Config class.

        Args:
            config_path (str): The path to the configuration file (default is ".env").
        """
        load_dotenv(config_path)
        self.db_host = self._get_env_variable("DB_HOST")
        self.db_port = self._get_env_variable("DB_PORT")
        self.db_name = self._get_env_variable("DB_NAME")
        self.db_user = self._get_env_variable("DB_USER")
        self.db_password = self._get_env_variable("DB_PASSWORD")

    def _get_env_variable(self, variable_name: str):
        """Get an environment variable and raise an exception if it is None.

        Args:
            variable_name (str): Name of the environment variable.

        Returns:
            str: The value of the environment variable.

        Raises:
            ValueError: If the environment variable is None.
        """
        value = os.getenv(variable_name)
        if value is None:
            raise ValueError(f"{variable_name} must be set in the .env file.")
        return value
