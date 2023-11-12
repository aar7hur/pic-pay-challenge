import os
from pathlib import Path
from typing import Dict

import pytest

from picpaychallenge.src.interface_adapters.config.config import Config


@pytest.fixture
def valid_config_data() -> Dict[str, str]:
    """Fixture for providing valid configuration data."""
    return {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "DB_NAME": "test_db",
        "DB_USER": "test_user",
        "DB_PASSWORD": "test_password",
    }


def _create_env_file(project_root_path: str, valid_config_data: Dict[str, str]):
    """Create a temporary .env file with valid configuration data."""
    with open(str(Path(project_root_path) / ".env"), "w") as env_file:
        env_file.write("\n".join([f"{key}={value}" for key, value in valid_config_data.items()]))


def _delete_file(project_root_path: str):
    """Delete the temporary .env file if it exists."""
    try:
        os.remove(str(Path(project_root_path) / ".env"))
    except FileNotFoundError:
        pass


def test_config_singleton_instance(project_root_path: str, valid_config_data: Dict[str, str]):
    """Test Config singleton instance creation."""
    # Arrange
    _delete_file(project_root_path)
    _create_env_file(project_root_path, valid_config_data)

    # Act
    config_instance_1 = Config()
    config_instance_2 = Config()

    # Assert
    assert config_instance_1 is config_instance_2


def test_config_instance_attributes(project_root_path: str, valid_config_data: Dict[str, str]):
    """Test Config instance attributes."""
    # Act
    _delete_file(project_root_path)
    _create_env_file(project_root_path, valid_config_data)
    config_instance = Config()

    # Assert
    assert config_instance.db_host == valid_config_data["DB_HOST"]
    assert config_instance.db_port == valid_config_data["DB_PORT"]
    assert config_instance.db_name == valid_config_data["DB_NAME"]
    assert config_instance.db_user == valid_config_data["DB_USER"]
    assert config_instance.db_password == valid_config_data["DB_PASSWORD"]
    _delete_file(project_root_path)
